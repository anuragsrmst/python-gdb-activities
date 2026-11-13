# Activity 24: SQLite Transaction Repository & Data Migration

## 1. Title
# Activity 24: SQLite Transaction Repository & Data Migration

## 2. Description
In core banking platforms like Kotak Mahindra Bank, financial transactions must provide ACID guarantees (Atomicity, Consistency, Isolation, Durability). When money is transferred between accounts, both the debit and the credit must either succeed together or fail together without leaving the ledger in an inconsistent state.

In this activity, you will implement `SqliteTransactionRepository` in Python to record immutable transaction audit logs and execute atomic multi-account funds transfers inside single database transactions with `commit` and `rollback` handling. Additionally, you will build `DataMigrator` to migrate accounts and audit records from in-memory repositories into persistent SQLite databases without data loss.

Moving the `transfer` operation into `TransactionRepository` ensures strict adherence to the Separation of Concerns principle.

By the end of this activity, you will be able to: execute multi-statement ACID database transactions in Python, implement atomic funds transfers with rollback error recovery, and migrate data across repository backends.

## 3. Topic Coverage
- **Python concepts**
  - Transaction control with `conn.commit()` and `conn.rollback()`
  - Structured error handling with `try / except / finally`
  - Data migration between different repository interfaces
- **Design patterns / architecture**
  - Unit of Work / ACID Transaction Pattern
  - Migration Engine Pattern
  - Separation of Concerns (Transaction Ledger & Transfers)
- **Domain concepts**
  - Atomic inter-account funds transfer
  - Immutable transaction audit logging
  - Repository-to-Repository data migration

## 4. Steps to Run the Activity
1. Navigate to the activity directory:
   ```bash
   cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity24
   ```
2. Run the SQLite transaction repository and migration test suite:
   ```bash
   python gdb/tests/test_sqlite_transaction_repository.py
   ```
3. Verify that transaction logging, atomic funds transfers, and repository data migrations succeed.

## 5. Target Files, Classes, Methods, Interfaces, Repos, Services

| Type | Name | Package | Status | Notes |
|------|------|---------|--------|-------|
| interface | `TransactionRepository` | `gdb.repository` | PROVIDED | Transaction ledger and transfer interface |
| class | `SqliteTransactionRepository` | `gdb.repository` | NEW | Relational transaction repository with ACID transfers |
| class | `DataMigrator` | `gdb.db` | NEW | In-memory to SQLite data migration engine |
| test | `test_sqlite_transaction_repository.py` | `gdb.tests` | NEW | Verification test suite |

## 6. Step-by-Step Instructions of Implementation

### STEP 1: Implement save(transaction)
- **Where:** `gdb/repository/sqlite_transaction_repository.py` — method `save(transaction)`
- **What:** Parameterized `INSERT INTO transactions (transaction_id, timestamp, account_number, transaction_type, amount, balance_after, status, description, from_account, to_account) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`.
- **Why:** Records transaction audit rows in the database.
- **Hint:** Acquire connection, execute query, commit, and close connection in `finally`.

### STEP 2: Implement find_by_account(account_number)
- **Where:** `gdb/repository/sqlite_transaction_repository.py` — method `find_by_account(account_number)`
- **What:** Query `SELECT * FROM transactions WHERE account_number = ? OR from_account = ? OR to_account = ? ORDER BY transaction_id ASC`.
- **Why:** Retrieves chronological transaction statements for a given account.
- **Hint:** Map rows to `Transaction` domain objects.

### STEP 3: Implement find_all()
- **Where:** `gdb/repository/sqlite_transaction_repository.py` — method `find_all()`
- **What:** Query `SELECT * FROM transactions ORDER BY transaction_id ASC` and return list of all transactions.
- **Why:** Enables system-wide audit reports.
- **Hint:** Fetch all rows and map them.

### STEP 4: Implement transfer(from_account, to_account, amount)
- **Where:** `gdb/repository/sqlite_transaction_repository.py` — method `transfer(from_account, to_account, amount)`
- **What:** Open a single connection, execute `UPDATE accounts SET balance = balance - ? WHERE account_number = ?`, `UPDATE accounts SET balance = balance + ? WHERE account_number = ?`, insert an audit log record into `transactions`, and call `conn.commit()`. On exception, call `conn.rollback()` and re-raise.
- **Why:** Guarantees atomic ACID transfers between accounts.
- **Hint:** Ensure both debit and credit execute within the same database transaction.

### STEP 5: Implement DataMigrator.migrate()
- **Where:** `gdb/db/data_migrator.py` — method `migrate(src_acc_repo, src_txn_repo, dest_acc_repo, dest_txn_repo)`
- **What:** Read all accounts and transactions from source repositories and save them into destination repositories.
- **Why:** Facilitates smooth migration from in-memory state to persistent SQLite databases.
- **Hint:** Return a dictionary with count statistics `{"accounts_migrated": n, "transactions_migrated": m}`.

## 7. Acceptance Criteria
- [ ] `SqliteTransactionRepository` records transaction audit logs with full metadata.
- [ ] `find_by_account` returns transactions where account is primary, sender, or receiver.
- [ ] `transfer` executes atomically with rollback on exception.
- [ ] `DataMigrator` successfully migrates all accounts and transactions without data corruption.
- [ ] Running `test_sqlite_transaction_repository.py` completes with all assertions passing.

## 8. Expected Output
```bash
$ python gdb/tests/test_sqlite_transaction_repository.py
```
```text
============================================================
  ACTIVITY 24 — SQLITE TRANSACTION REPOSITORY & MIGRATION
============================================================
[TEST 1] Transaction Save & Query:
  Found transactions for #1001: 1
  -> PASSED

[TEST 2] Atomic Transfer Execution:
  Updated Sender Balance: Rs. 40000.0 (Expected: 40000.0)
  Updated Receiver Balance: Rs. 40000.0 (Expected: 40000.0)
  -> PASSED

[TEST 3] Data Migration from Memory to SQLite:
  Migrated stats: {'accounts_migrated': 1, 'transactions_migrated': 0}
  -> PASSED

============================================================
  🎉 ALL 3/3 ACTIVITY 24 TESTS PASSED! Excellent work!
============================================================
```

## 9. How to Run the Commands
```bash
# 1. Navigate to activity root
cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity24

# 2. Run test driver
python gdb/tests/test_sqlite_transaction_repository.py

# 3. Clean up test database
rm -f test_txn_repo.db
```
Verify success by confirming all 3 tests pass as described in Section 7.

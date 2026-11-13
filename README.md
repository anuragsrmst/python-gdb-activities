# Activity 23: SQLite Account Repository (CRUD Operations)

## 1. Title
# Activity 23: SQLite Account Repository (CRUD Operations)

## 2. Description
In enterprise banking systems like Axis Bank, customer account data must be persisted to a relational database using parameterized SQL queries. Parameterized queries prevent catastrophic SQL injection attacks and allow relational databases to cache compiled execution plans.

In this activity, you will implement `SqliteAccountRepository` in Python to fulfill the `AccountRepository` contract using SQLite. You will execute parameterized SQL statements for single-entity account CRUD operations (Create, Read, Update, Delete), map database result rows back to polymorphic domain `Account` objects, and compute sequential account IDs using SQL `MAX()`.

Following the Separation of Concerns principle, this repository handles single-account records exclusively and delegates financial transfers to the transaction repository.

By the end of this activity, you will be able to: write secure parameterized SQL queries in Python, map relational rows to domain objects, and manage database connection lifecycles safely.

## 3. Topic Coverage
- **Python concepts**
  - Parameterized query execution with `cursor.execute(sql, params)`
  - Safe cursor and connection cleanup via `try / finally`
  - Mapping `sqlite3.Row` dictionary-like objects to domain entities
- **Design patterns / architecture**
  - Repository Pattern with relational database backing
  - Data Mapper Pattern for entity reconstruction
  - Separation of Concerns (Single-Entity CRUD)
- **Domain concepts**
  - Account persistence lifecycle (Creation, Modification, Deletion)
  - Account status management (Active, Inactive/Closed)
  - Next sequential account ID generation via database aggregation

## 4. Steps to Run the Activity
1. Navigate to the activity directory:
   ```bash
   cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity23
   ```
2. Run the SQLite account repository test suite:
   ```bash
   python gdb/tests/test_sqlite_account_repository.py
   ```
3. Verify that account insertion, lookup, balance update, deletion, and sequence generation succeed.

## 5. Target Files, Classes, Methods, Interfaces, Repos, Services

| Type | Name | Package | Status | Notes |
|------|------|---------|--------|-------|
| interface | `AccountRepository` | `gdb.repository` | PROVIDED | Single-entity account CRUD interface |
| class | `SqliteAccountRepository` | `gdb.repository` | NEW | Relational account repository executing SQL queries |
| test | `test_sqlite_account_repository.py` | `gdb.tests` | NEW | Verification test suite |

## 6. Step-by-Step Instructions of Implementation

### STEP 1: Implement save(account)
- **Where:** `gdb/repository/sqlite_account_repository.py` — method `save(account)`
- **What:** Execute parameterized `INSERT INTO accounts (account_number, account_holder_name, age, balance, account_type, status, pin, opening_date, overdraft_used, interest_earned) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`.
- **Why:** Saves new account entities into the relational database.
- **Hint:** Acquire connection from `self.provider.get_connection()`, execute query, commit, and close connection in `finally`.

### STEP 2: Implement find_by_id(account_number)
- **Where:** `gdb/repository/sqlite_account_repository.py` — method `find_by_id(account_number)`
- **What:** Query `SELECT * FROM accounts WHERE account_number = ?`. If found, map row via `self._map_row(row)` to `IAccount`.
- **Why:** Fetches an account by its unique primary key.
- **Hint:** Use `AccountFactory.create_account(...)` to reconstruct the polymorphic domain object.

### STEP 3: Implement find_all()
- **Where:** `gdb/repository/sqlite_account_repository.py` — method `find_all()`
- **What:** Query `SELECT * FROM accounts` and map all rows to a list of `IAccount`.
- **Why:** Supports bulk reporting and reconciliation workflows.
- **Hint:** Iterate over `cursor.fetchall()`.

### STEP 4: Implement update(account)
- **Where:** `gdb/repository/sqlite_account_repository.py` — method `update(account)`
- **What:** Execute `UPDATE accounts SET balance = ?, status = ?, overdraft_used = ?, interest_earned = ? WHERE account_number = ?`.
- **Why:** Persists balance changes and status modifications to disk.
- **Hint:** Commit transaction after updating.

### STEP 5: Implement delete(account_number)
- **Where:** `gdb/repository/sqlite_account_repository.py` — method `delete(account_number)`
- **What:** Execute `DELETE FROM accounts WHERE account_number = ?`.
- **Why:** Allows purging closed accounts from the database.
- **Hint:** Commit transaction and close connection.

### STEP 6: Implement exists(account_number)
- **Where:** `gdb/repository/sqlite_account_repository.py` — method `exists(account_number)`
- **What:** Execute `SELECT 1 FROM accounts WHERE account_number = ?` and return `cursor.fetchone() is not None`.
- **Why:** Provides lightweight O(1) existence checks without mapping full objects.
- **Hint:** Do not fetch unused columns.

### STEP 7: Implement next_account_number()
- **Where:** `gdb/repository/sqlite_account_repository.py` — method `next_account_number()`
- **What:** Execute `SELECT COALESCE(MAX(account_number), 1000) + 1 FROM accounts` and return integer result.
- **Why:** Generates unique sequential account numbers from database state.
- **Hint:** Handle empty table gracefully with `COALESCE`.

## 7. Acceptance Criteria
- [ ] `SqliteAccountRepository` contains pure single-entity account CRUD operations.
- [ ] Parameterized queries (`?`) are used exclusively to prevent SQL injection vulnerabilities.
- [ ] `find_by_id` accurately maps database rows to polymorphic `SavingsAccount` and `CurrentAccount` entities.
- [ ] `update` synchronizes balance and account status reliably.
- [ ] `next_account_number` computes `MAX(account_number) + 1` from the database.
- [ ] Running `test_sqlite_account_repository.py` passes 100% of test assertions.

## 8. Expected Output
```bash
$ python gdb/tests/test_sqlite_account_repository.py
```
```text
============================================================
  ACTIVITY 23 — SQLITE ACCOUNT REPOSITORY CRUD TESTS
============================================================
[TEST 1] Save & FindById:
  Found: Account #1001 | Rajesh Sharma (30 yrs, Tenure: 0 yrs) | Savings | Rs. 50000.0 | Active
  -> PASSED

[TEST 2] Update & FindAll:
  Updated balance: Rs. 65000.0 (Expected: 65000.0)
  Total accounts in DB: 2 (Expected: 2)
  -> PASSED

[TEST 3] Delete & Exists:
  Account 1002 successfully deleted.
  -> PASSED

============================================================
  🎉 ALL 3/3 ACTIVITY 23 SQLITE ACCOUNT REPOSITORY TESTS PASSED!
============================================================
```

## 9. How to Run the Commands
```bash
# 1. Navigate to activity root
cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity23

# 2. Run test driver
python gdb/tests/test_sqlite_account_repository.py

# 3. Clean up test database
rm -f test_acc_repo.db
```
Verify success by confirming all 3 tests pass as described in Section 7.

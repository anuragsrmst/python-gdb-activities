# Activity 26: File Repository (CSV + Atomic Writes + Rolling Backups)

## 1. Title
# Activity 26: File Repository (CSV + Atomic Writes + Rolling Backups)

## 2. Description
In edge banking terminals, disaster recovery standbys, and audit export pipelines across banks like ICICI Bank, financial data must be stored in structured flat files (CSV). If a power outage or application crash occurs while writing a file directly, the entire dataset can be corrupted.

In this activity, you will implement crash-resilient file persistence for GDB in Python. You will build `AtomicFileWriter` using temporary files and atomic rename operations (`os.replace`) to ensure zero-corruption writes, implement `BackupManager` for timestamped rolling backup rotations, and build `FileAccountRepository` and `FileTransactionRepository` conforming to standard repository interfaces.

Following the Separation of Concerns principle, `FileAccountRepository` handles single-entity account CRUD while `FileTransactionRepository` manages transaction logging and transfers.

By the end of this activity, you will be able to: serialize domain entities to CSV format, execute crash-proof atomic file writes in Python, manage automated rolling file backups, and implement file-backed repositories.

## 3. Topic Coverage
- **Python concepts**
  - File I/O operations with `open()` and context managers
  - Safe atomic file replacement with `os.replace`
  - Directory scanning, sorting, and pruning with `os.listdir` and `os.remove`
- **Design patterns / architecture**
  - Atomic Write Pattern
  - Rolling Backup / Retention Pattern
  - Repository Pattern with CSV file backing
- **Domain concepts**
  - Flat-file account persistence
  - Transaction ledger CSV serialization
  - File-based atomic funds transfer

## 4. Steps to Run the Activity
1. Navigate to the activity directory:
   ```bash
   cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity26
   ```
2. Run the file repository test suite:
   ```bash
   python gdb/tests/test_file_repository.py
   ```
3. Verify that account persistence, atomic updates, transaction logging, and atomic transfers pass.

## 5. Target Files, Classes, Methods, Interfaces, Repos, Services

| Type | Name | Package | Status | Notes |
|------|------|---------|--------|-------|
| class | `AtomicFileWriter` | `gdb.file` | NEW | Crash-resilient file writer using temporary files |
| class | `CsvMapper` | `gdb.file` | NEW | CSV serialization and deserialization for accounts |
| class | `BackupManager` | `gdb.file` | NEW | Timestamped rolling backup rotation manager |
| repo | `FileAccountRepository` | `gdb.repository` | NEW | CSV-backed account repository (CRUD) |
| repo | `FileTransactionRepository` | `gdb.repository` | NEW | CSV-backed transaction ledger and transfer repo |
| test | `test_file_repository.py` | `gdb.tests` | NEW | Verification test suite |

## 6. Step-by-Step Instructions of Implementation

### STEP 1: Implement AtomicFileWriter
- **Where:** `gdb/file/atomic_file_writer.py` — method `write_lines(file_path, lines)`
- **What:** Write lines to a temporary file `file_path + ".tmp." + str(time.time_ns())`, flush and sync buffers, then atomically rename to `file_path` using `os.replace()`.
- **Why:** Protects against incomplete file corruption during unexpected crashes.
- **Hint:** Use `os.replace(temp_path, file_path)`.

### STEP 2: Implement CsvMapper
- **Where:** `gdb/file/csv_mapper.py` — methods `to_csv(account)` and `from_csv(line)`
- **What:** Convert domain `Account` entities to and from comma-separated string representations.
- **Why:** Standardizes flat-file entity serialization.
- **Hint:** Split line by comma and parse appropriate types (int, float, str).

### STEP 3: Implement BackupManager
- **Where:** `gdb/file/backup_manager.py` — method `create_backup(file_path, max_backups)`
- **What:** Copy `file_path` to `file_path + ".bak." + timestamp` and prune oldest backups if the count exceeds `max_backups`.
- **Why:** Preserves historical snapshots and prevents unbounded disk usage.
- **Hint:** Sort backup files by modification time and delete excess files.

### STEP 4: Implement FileAccountRepository
- **Where:** `gdb/repository/file_account_repository.py`
- **What:** Implement `save()`, `find_by_id()`, `find_all()`, `update()`, `delete()`, `exists()`, and `next_account_number()` reading and writing `accounts.csv`.
- **Why:** Provides full account CRUD persistence backed by CSV storage.
- **Hint:** Delegate atomic file writes to `AtomicFileWriter`.

### STEP 5: Implement FileTransactionRepository
- **Where:** `gdb/repository/file_transaction_repository.py`
- **What:** Implement `save()`, `find_by_account()`, `find_all()`, `clear()`, and `transfer()` for `transactions.csv`.
- **Why:** Records transaction ledgers and executes file-based funds transfers.
- **Hint:** In `transfer`, update both accounts and append transaction record.

## 7. Acceptance Criteria
- [ ] `AtomicFileWriter` writes to temporary files before atomic replacement.
- [ ] `BackupManager` creates timestamped backups and enforces retention limits.
- [ ] `FileAccountRepository` performs accurate CRUD operations without corrupting CSV headers.
- [ ] `FileTransactionRepository` appends audit logs and executes transfers cleanly.
- [ ] Running `test_file_repository.py` passes 100% of test assertions.

## 8. Expected Output
```bash
$ python gdb/tests/test_file_repository.py
```
```text
============================================================
  ACTIVITY 26 — FILE REPOSITORY (CSV + ATOMIC WRITES + BACKUP)
============================================================
[TEST 1] Account Save & Read Back from CSV:
  Saved: Account #1001 | Rajesh Sharma (30 yrs, Tenure: 0 yrs) | Savings | Rs. 50000.0 | Active
  Found: Account #1001 | Rajesh Sharma (30 yrs, Tenure: 0 yrs) | Savings | Rs. 50000.0 | Active
  -> PASSED

[TEST 2] Multiple Accounts & Atomic Update:
  Updated balance: Rs. 60000.0 (Expected: 60000.0)
  -> PASSED

[TEST 3] Transaction Save & Query in CSV:
  Found transactions for #1001: 1 (Expected: 1)
  -> PASSED

[TEST 4] Atomic Transfer via FileTransactionRepository:
  Sender balance: Rs. 55000.0 (Expected: 55000.0)
  Receiver balance: Rs. 45000.0 (Expected: 45000.0)
  -> PASSED

============================================================
  🎉 ALL 4/4 ACTIVITY 26 FILE REPOSITORY TESTS PASSED!
============================================================
```

## 9. How to Run the Commands
```bash
# 1. Navigate to activity root
cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity26

# 2. Run test driver
python gdb/tests/test_file_repository.py

# 3. Clean up test files
rm -rf test_data/
```
Verify success by confirming all 4 tests pass as described in Section 7.

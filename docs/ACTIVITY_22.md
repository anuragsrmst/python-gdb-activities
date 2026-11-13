# Activity 22: SQLite Connection & Schema Initialization

## 1. Title
# Activity 22: SQLite Connection & Schema Initialization

## 2. Description
In production banking platforms such as State Bank of India (SBI), storing accounts and financial records only in memory is unacceptable because server restarts would wipe out all customer funds. Systems must persist data reliably to relational databases.

In this activity, you will establish the relational database foundation for GDB using Python's built-in DB-API 2.0 module (`sqlite3`). You will create `SqliteConnectionProvider` to supply database connections configured with row-level dictionary mapping (`sqlite3.Row`), and implement `SchemaInitializer` to execute idempotent Data Definition Language (DDL) scripts that create the tables for accounts and transaction ledgers.

Setting up idempotent schema scripts ensures that database tables are created automatically without throwing errors if the tables already exist.

By the end of this activity, you will be able to: manage relational database connections in Python, configure dictionary-based result set row factories, and execute idempotent DDL schema scripts.

## 3. Topic Coverage
- **Python concepts**
  - Database connectivity with standard `sqlite3`
  - Result row mapping with `sqlite3.Row`
  - Safe resource handling with `try / finally` blocks
- **Design patterns / architecture**
  - Provider Pattern for database connections
  - Database Migration / Schema Initializer Pattern
  - Idempotent script execution
- **Domain concepts**
  - Relational schema modeling for core accounts
  - Relational schema modeling for transaction audit logs
  - Foreign key and data integrity constraints

## 4. Steps to Run the Activity
1. Navigate to the activity directory:
   ```bash
   cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity22
   ```
2. Run the connection and schema initialization test:
   ```bash
   python gdb/tests/test_sqlite_connection.py
   ```
3. Verify that database connections open successfully and that tables `accounts` and `transactions` are created.

## 5. Target Files, Classes, Methods, Interfaces, Repos, Services

| Type | Name | Package | Status | Notes |
|------|------|---------|--------|-------|
| interface | `ConnectionProvider` | `gdb.db` | NEW | Base interface for acquiring database connections |
| class | `SqliteConnectionProvider` | `gdb.db` | NEW | Concrete SQLite connection provider with row factory |
| class | `SchemaInitializer` | `gdb.db` | NEW | DDL execution engine for database tables |
| test | `test_sqlite_connection.py` | `gdb.tests` | NEW | Verification test driver |

## 6. Step-by-Step Instructions of Implementation

### STEP 1: Implement SqliteConnectionProvider
- **Where:** `gdb/db/sqlite_connection_provider.py` — method `get_connection()`
- **What:** Open a connection to `self.db_path` using `sqlite3.connect()`, set `conn.row_factory = sqlite3.Row`, and return the connection.
- **Why:** Enables column-name indexed access on returned query rows.
- **Hint:** `conn = sqlite3.connect(self.db_path); conn.row_factory = sqlite3.Row; return conn`

### STEP 2: Implement SchemaInitializer
- **Where:** `gdb/db/schema_initializer.py` — method `initialize(provider)`
- **What:** Obtain a connection from `provider.get_connection()`, execute `CREATE TABLE IF NOT EXISTS accounts (...)` and `CREATE TABLE IF NOT EXISTS transactions (...)`, commit the transaction, and close the connection.
- **Why:** Automatically establishes database structure before repository operations begin.
- **Hint:** Use multi-line SQL DDL strings and execute with `cursor.execute()`.

## 7. Acceptance Criteria
- [ ] `SqliteConnectionProvider` establishes valid SQLite database connections.
- [ ] `conn.row_factory` is set to `sqlite3.Row` for intuitive column indexing.
- [ ] `SchemaInitializer.initialize()` creates table `accounts` with proper column data types.
- [ ] `SchemaInitializer.initialize()` creates table `transactions` with proper column data types.
- [ ] Schema execution is idempotent (`CREATE TABLE IF NOT EXISTS`) and does not crash on repeated runs.
- [ ] Running `test_sqlite_connection.py` passes all assertions.

## 8. Expected Output
```bash
$ python gdb/tests/test_sqlite_connection.py
```
```text
============================================================
  ACTIVITY 22 — SQLITE CONNECTION & SCHEMA INITIALIZATION
============================================================
[TEST 1] Database Connection Establishment:
  Connected to: test_conn_gdb.db
  -> PASSED

[TEST 2 & 3] Schema DDL Execution & Verification:
  Verified tables in DB: ['accounts', 'transactions']
  -> PASSED (DDL initialized and verified)

============================================================
  🎉 ALL 3/3 ACTIVITY 22 TESTS PASSED! Great job!
============================================================
```

## 9. How to Run the Commands
```bash
# 1. Navigate to activity root
cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity22

# 2. Run test driver
python gdb/tests/test_sqlite_connection.py

# 3. Clean up test database
rm -f test_conn_gdb.db
```
Verify success by confirming all 3 tests pass as described in Section 7.

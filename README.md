# Activity 21: Repository Pattern – In-Memory Storage & Factory

## 1. Title
# Activity 21: Repository Pattern – In-Memory Storage & Factory

## 2. Description
In modern banking architectures like those at HDFC and ICICI Bank, core business services must never directly touch raw storage media or SQL drivers. When an account is opened, deposited into, or audited, the business layer talks to an abstraction called the Repository Pattern. This isolates your business rules from the underlying storage mechanism.

In this activity, you will build the foundational repository layer for the Global Digital Banking (GDB) system in Python. You will define the abstract contracts for `AccountRepository` and `TransactionRepository`, implement thread-safe in-memory backings (`InMemoryAccountRepository` and `InMemoryTransactionRepository`), and build a configurable `RepositoryFactory` to dynamically supply storage providers.

Separating single-entity account CRUD from transaction logging and multi-account transfers ensures strict compliance with the Single Responsibility Principle (SRP).

By the end of this activity, you will be able to: decouple data storage from business logic using the Repository Pattern, ensure thread-safe in-memory state manipulation with `threading.RLock`, and instantiate repositories dynamically using the Factory Pattern.

## 3. Topic Coverage
- **Python concepts**
  - Abstract base classes with `@abstractmethod` via the `abc` module
  - Thread synchronization using `threading.RLock`
  - In-memory dictionary and list manipulations with defensive copying
- **Design patterns / architecture**
  - Repository Pattern for domain data abstraction
  - Factory Pattern for storage provider instantiation
  - Separation of Concerns (CRUD vs Multi-Account Ledger)
- **Domain concepts**
  - Single-entity account lifecycle management
  - Transaction audit trail tracking
  - Sequence generation for unique account IDs

## 4. Steps to Run the Activity
1. Navigate to the activity directory:
   ```bash
   cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity21
   ```
2. Run the in-memory repository test suite:
   ```bash
   python gdb/tests/test_repository_in_memory.py
   ```
3. Verify that all account CRUD operations, transaction logs, and service integration tests succeed.

## 5. Target Files, Classes, Methods, Interfaces, Repos, Services

| Type | Name | Package | Status | Notes |
|------|------|---------|--------|-------|
| interface | `AccountRepository` | `gdb.repository` | NEW | Contract for single-entity account CRUD |
| interface | `TransactionRepository` | `gdb.repository` | NEW | Contract for transaction ledger and atomic transfers |
| class | `InMemoryAccountRepository` | `gdb.repository` | NEW | Thread-safe dictionary-backed account repository |
| class | `InMemoryTransactionRepository` | `gdb.repository` | NEW | Thread-safe list-backed transaction ledger |
| class | `RepositoryFactory` | `gdb.repository` | NEW | Factory instantiating repository backends |
| service | `AccountService` | `gdb.service` | UPDATE | Refactored service delegating to repositories |
| test | `test_repository_in_memory.py` | `gdb.tests` | NEW | Verification test driver |

## 6. Step-by-Step Instructions of Implementation

### STEP 1: Initialize In-Memory Account Repository
- **Where:** `gdb/repository/in_memory_account_repository.py` — method `__init__()`
- **What:** Initialize an internal dictionary `self._storage: Dict[int, IAccount] = {}`, a re-entrant lock `self._lock = threading.RLock()`, and sequence counter `self._next_id = 1001`.
- **Why:** Prepares the in-memory data store for thread-safe operations.
- **Hint:** Use `threading.RLock()` to allow re-entrant method calls within the same thread.

### STEP 2: Implement save(account)
- **Where:** `gdb/repository/in_memory_account_repository.py` — method `save(account)`
- **What:** Store the provided `account` into `self._storage` keyed by its account number under lock.
- **Why:** Persists newly created domain accounts.
- **Hint:** `with self._lock: self._storage[account.get_account_number()] = account`

### STEP 3: Implement find_by_id(account_number)
- **Where:** `gdb/repository/in_memory_account_repository.py` — method `find_by_id(account_number)`
- **What:** Return the `IAccount` instance matching `account_number`, or `None` if not found.
- **Why:** Enables fetching individual account records by primary key.
- **Hint:** Use `self._storage.get(account_number)`.

### STEP 4: Implement find_all()
- **Where:** `gdb/repository/in_memory_account_repository.py` — method `find_all()`
- **What:** Return a shallow copy list of all accounts currently stored.
- **Why:** Protects internal dictionary state from external mutation.
- **Hint:** Return `list(self._storage.values())`.

### STEP 5: Implement update(account)
- **Where:** `gdb/repository/in_memory_account_repository.py` — method `update(account)`
- **What:** Update the account in `self._storage` if it exists.
- **Why:** Synchronizes balance or status updates to storage.
- **Hint:** Acquire `self._lock` before updating dictionary entries.

### STEP 6: Implement delete(account_number)
- **Where:** `gdb/repository/in_memory_account_repository.py` — method `delete(account_number)`
- **What:** Remove the account entry matching `account_number` from `self._storage` if present.
- **Why:** Supports account closure and purging workflows.
- **Hint:** Use `self._storage.pop(account_number, None)`.

### STEP 7: Implement exists(account_number)
- **Where:** `gdb/repository/in_memory_account_repository.py` — method `exists(account_number)`
- **What:** Return `True` if `account_number` exists in `self._storage`, else `False`.
- **Why:** Provides fast O(1) membership checking.
- **Hint:** `return account_number in self._storage`

### STEP 8: Implement next_account_number()
- **Where:** `gdb/repository/in_memory_account_repository.py` — method `next_account_number()`
- **What:** Atomically increment and return the next account number sequence.
- **Why:** Guarantees unique auto-incremented account numbers.
- **Hint:** `with self._lock: val = self._next_id; self._next_id += 1; return val`

### STEP 9: Implement InMemoryTransactionRepository
- **Where:** `gdb/repository/in_memory_transaction_repository.py`
- **What:** Implement `save()`, `find_by_account()`, `find_all()`, `clear()`, and `transfer()` using an internal list protected by `threading.RLock`.
- **Why:** Maintains an immutable chronological audit trail of all banking transactions.
- **Hint:** Filter transactions in `find_by_account` where `t.get_account_number() == acc` or `from_account == acc` or `to_account == acc`.

## 7. Acceptance Criteria
- [ ] `AccountRepository` strictly declares single-entity CRUD operations and does NOT contain `transfer`.
- [ ] `TransactionRepository` declares transaction ledger querying, saving, and `transfer`.
- [ ] `InMemoryAccountRepository` correctly persists, retrieves, updates, and deletes account entities.
- [ ] `InMemoryTransactionRepository` maintains chronological transaction audit history.
- [ ] All in-memory read and write operations are synchronized with `threading.RLock`.
- [ ] Running `test_repository_in_memory.py` passes 100% of test assertions.

## 8. Expected Output
```bash
$ python gdb/tests/test_repository_in_memory.py
```
```text
============================================================
  ACTIVITY 21 — REPOSITORY PATTERN IN-MEMORY TESTS (PYTHON)
============================================================
[TEST 1] Account Repository CRUD:
  Saved: Account #1001 | Rajesh Sharma (30 yrs, Tenure: 0 yrs) | Savings | Rs. 50000.0 | Active
  Updated balance: Rs. 65000.0
  Total accounts in repository: 2
  -> PASSED

[TEST 2] Transaction Repository Operations:
  Found transactions for #1001: 2
  -> PASSED

[TEST 3] Service Integration with Repositories:
  Opened account #1001 via AccountService.
  Deposit executed. New Balance: Rs. 25000.0
  -> PASSED

============================================================
  🎉 ALL 3/3 ACTIVITY 21 TESTS PASSED! Excellent work!
============================================================
```

## 9. How to Run the Commands
```bash
# 1. Navigate to activity root
cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity21

# 2. Run test driver
python gdb/tests/test_repository_in_memory.py
```
Verify success by confirming all 3 tests pass as described in Section 7.

# Activity 28: Locks, Atomics & Concurrent Collections

## 1. Title
# Activity 28: Locks, Atomics & Concurrent Collections

## 2. Description
While a single global lock ensures thread safety, it creates severe performance bottlenecks in production banking systems like Axis Bank because operations on completely unrelated customer accounts block each other unnecessarily.

In this activity, you will replace coarse-grained global locks with fine-grained per-account locks and atomic sequences. You will build `AccountLockRegistry` to maintain a registry of per-account `RLock` instances, implement `LockedAccountService` with deadlock-free ordered lock acquisition for bidirectional transfers, and create `AtomicAccountService` for high-throughput atomic sequence generation.

Ordering lock acquisition by account number (`min(acc1, acc2)` then `max(acc1, acc2)`) completely eliminates circular wait deadlocks during concurrent inter-account transfers.

By the end of this activity, you will be able to: implement fine-grained per-entity locking in Python, prevent multithreaded deadlocks using resource ordering, and generate thread-safe atomic sequences.

## 3. Topic Coverage
- **Python concepts**
  - Fine-grained synchronization with per-account `threading.RLock`
  - Context managers with `__enter__` and `__exit__`
  - Deadlock prevention via deterministic resource ordering
- **Design patterns / architecture**
  - Lock Striping / Registry Pattern
  - Deadlock-Free Resource Hierarchy Pattern
  - Atomic Sequence Generator Pattern
- **Domain concepts**
  - Parallel multi-account banking transactions
  - Bidirectional concurrent transfers between accounts
  - Collision-free transaction ID allocation

## 4. Steps to Run the Activity
1. Navigate to the activity directory:
   ```bash
   cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity28
   ```
2. Run the locks and atomics test suite:
   ```bash
   python gdb/tests/test_locks_and_atomics.py
   ```
3. Verify that independent accounts execute in parallel, transfers never deadlock, and sequence IDs are collision-free.

## 5. Target Files, Classes, Methods, Interfaces, Repos, Services

| Type | Name | Package | Status | Notes |
|------|------|---------|--------|-------|
| class | `AccountLockRegistry` | `gdb.concurrency` | NEW | Fine-grained lock registry per account number |
| class | `AccountLock` | `gdb.concurrency` | NEW | Context manager wrapper for lock handling |
| service | `LockedAccountService` | `gdb.service` | NEW | Service utilizing fine-grained locks and ordered transfers |
| service | `AtomicAccountService` | `gdb.service` | NEW | Service providing thread-safe atomic sequence counters |
| test | `test_locks_and_atomics.py` | `gdb.tests` | NEW | Verification test suite |

## 6. Step-by-Step Instructions of Implementation

### STEP 1: Implement AccountLockRegistry
- **Where:** `gdb/concurrency/account_lock_registry.py` — method `get_lock(account_number)`
- **What:** Maintain an internal dictionary of `threading.RLock` objects, creating and caching a lock for each `account_number` under registry lock.
- **Why:** Provides dedicated lock instances per account.
- **Hint:** `with self._registry_lock: if acc not in self._locks: self._locks[acc] = threading.RLock(); return self._locks[acc]`.

### STEP 2: Implement AccountLock Context Manager
- **Where:** `gdb/concurrency/account_lock.py` — methods `__enter__()` and `__exit__()`
- **What:** Acquire the lock in `__enter__` and release it in `__exit__`.
- **Why:** Enables clean `with AccountLock(registry, acc_num):` syntax.
- **Hint:** Return `self` from `__enter__`.

### STEP 3: Implement LockedAccountService with Ordered Locking
- **Where:** `gdb/service/locked_account_service.py` — method `transfer(from_acc, to_acc, amount)`
- **What:** Compute `first = min(from_acc, to_acc)` and `second = max(from_acc, to_acc)`. Acquire `first` lock, then `second` lock, then execute debit and credit.
- **Why:** Deterministic lock hierarchy prevents circular wait deadlocks.
- **Hint:** Always acquire lower account number lock first.

### STEP 4: Implement AtomicAccountService
- **Where:** `gdb/service/atomic_account_service.py` — method `next_transaction_id()`
- **What:** Atomically increment internal sequence counter under lock and return generated ID.
- **Why:** Guarantees collision-free unique IDs under high concurrency.
- **Hint:** Protect sequence increment with `threading.Lock()`.

## 7. Acceptance Criteria
- [ ] `AccountLockRegistry` returns dedicated `RLock` instances per account number.
- [ ] Operations on different accounts run concurrently without thread contention.
- [ ] Bidirectional concurrent transfers between two accounts never deadlock.
- [ ] Total combined balance of accounts is conserved across all transfer operations.
- [ ] `AtomicAccountService` generates 100% collision-free sequential IDs.
- [ ] Running `test_locks_and_atomics.py` passes all test assertions.

## 8. Expected Output
```bash
$ python gdb/tests/test_locks_and_atomics.py
```
```text
============================================================
  ACTIVITY 28 — LOCKS, ATOMICS & CONCURRENT COLLECTIONS (PYTHON)
============================================================
[TEST 1] Fine-Grained Per-Account Locking (Same Account):
  Expected Balance: Rs. 110000.0, Actual: Rs. 110000.0
  -> PASSED

[TEST 2] Deadlock-Free Bidirectional Transfers:
  Total Combined Balance Preserved: Rs. 200000.0
  -> PASSED

[TEST 3] Lock-Free Atomic Sequence Counter:
  Generated 1000 unique transaction IDs concurrently.
  -> PASSED

============================================================
  🎉 ALL 3/3 ACTIVITY 28 TESTS PASSED!
============================================================
```

## 9. How to Run the Commands
```bash
# 1. Navigate to activity root
cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity28

# 2. Run test driver
python gdb/tests/test_locks_and_atomics.py
```
Verify success by confirming all 3 tests pass as described in Section 7.

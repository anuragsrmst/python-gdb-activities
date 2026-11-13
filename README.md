# Activity 27: Concurrency – Thread Safety & Synchronization

## 1. Title
# Activity 27: Concurrency – Thread Safety & Synchronization

## 2. Description
In multi-channel banking systems like SBI where mobile apps, net banking, ATMs, and UPI gateways access the same bank account simultaneously, concurrent operations without proper synchronization cause disastrous race conditions and lost updates.

In this activity, you will demonstrate and resolve concurrent race conditions in Python. You will build `ConcurrentDepositDemo` using `threading.Event` synchronization barriers to unleash multiple worker threads simultaneously against an unsynchronized account, demonstrating lost deposits. Then, you will implement `ThreadSafeAccountService` with re-entrant synchronization (`threading.RLock`) to guarantee 100% balance integrity.

Eliminating lost updates ensures that every rupee deposited into a customer account is accurately credited regardless of concurrency.

By the end of this activity, you will be able to: simulate multithreaded race conditions using coordination barriers, diagnose lost update anomalies, and apply re-entrant synchronization locks to protect critical sections.

## 3. Topic Coverage
- **Python concepts**
  - Multithreading with `threading.Thread`
  - Synchronization barriers with `threading.Event`
  - Mutual exclusion using `threading.RLock`
- **Design patterns / architecture**
  - Thread-Safe Service Decorator / Wrapper Pattern
  - Barrier Synchronization Pattern
  - Concurrency testing and race condition diagnosis
- **Domain concepts**
  - Lost update anomaly in banking balances
  - Concurrent deposit and withdrawal processing
  - Account state consistency under heavy thread load

## 4. Steps to Run the Activity
1. Navigate to the activity directory:
   ```bash
   cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity27
   ```
2. Run the concurrency and synchronization test suite:
   ```bash
   python gdb/tests/test_concurrency.py
   ```
3. Verify that concurrent deposits against `ThreadSafeAccountService` calculate the exact expected final balance without lost updates.

## 5. Target Files, Classes, Methods, Interfaces, Repos, Services

| Type | Name | Package | Status | Notes |
|------|------|---------|--------|-------|
| class | `ConcurrentDepositDemo` | `gdb.concurrency` | NEW | Multithreaded race condition simulation harness |
| service | `ThreadSafeAccountService` | `gdb.service` | NEW | Synchronized account service wrapper |
| test | `test_concurrency.py` | `gdb.tests` | NEW | Verification test suite |

## 6. Step-by-Step Instructions of Implementation

### STEP 1: Implement ConcurrentDepositDemo
- **Where:** `gdb/concurrency/concurrent_deposit_demo.py` — method `run_concurrent_deposits(service, account_number, threads, deposits_per_thread, amount)`
- **What:** Create `start_event = threading.Event()`. Spawn `threads` worker threads waiting on `start_event.wait()` before executing deposit loops. Trigger `start_event.set()` to unleash threads simultaneously, call `join()` on all threads, and return final account balance.
- **Why:** Reliably exposes race conditions by ensuring simultaneous thread entry.
- **Hint:** Create and start threads in a list, then call `start_event.set()`, then `join()`.

### STEP 2: Implement ThreadSafeAccountService
- **Where:** `gdb/service/thread_safe_account_service.py`
- **What:** Wrap all modifying methods (`deposit()`, `withdraw()`, `transfer()`, `close_account()`) inside `with self._sync_lock:` blocks.
- **Why:** Enforces mutual exclusion so only one thread modifies account state at a time.
- **Hint:** Initialize `self._sync_lock = threading.RLock()`.

## 7. Acceptance Criteria
- [ ] `ConcurrentDepositDemo` uses `threading.Event` barrier to launch threads concurrently.
- [ ] `ThreadSafeAccountService` protects critical sections using `threading.RLock`.
- [ ] Concurrent deposits against `ThreadSafeAccountService` produce zero lost updates.
- [ ] Final balance matches exact calculation: `initial_balance + (threads * deposits_per_thread * amount)`.
- [ ] Running `test_concurrency.py` passes all assertions.

## 8. Expected Output
```bash
$ python gdb/tests/test_concurrency.py
```
```text
============================================================
  ACTIVITY 27 — CONCURRENCY & THREAD SAFETY TESTS (PYTHON)
============================================================
[TEST 1] Concurrent Deposits to Same Account:
  Spawning 10 threads, each making 100 deposits of Rs. 100.0...
  Initial Balance: Rs. 10000.0
  Expected Final Balance: Rs. 110000.0
  Actual Final Balance:   Rs. 110000.0
  -> PASSED (Zero lost updates!)

============================================================
  🎉 ALL ACTIVITY 27 CONCURRENCY TESTS PASSED! Excellent work!
============================================================
```

## 9. How to Run the Commands
```bash
# 1. Navigate to activity root
cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity27

# 2. Run test driver
python gdb/tests/test_concurrency.py
```
Verify success by confirming all tests pass as described in Section 7.

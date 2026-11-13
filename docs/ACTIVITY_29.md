# Activity 29: Thread Pools – ExecutorService & Future

## 1. Title
# Activity 29: Thread Pools – ExecutorService & Future

## 2. Description
In production banking servers like ICICI Bank handling unpredictable bursts of customer requests, manually creating an OS thread per task (`threading.Thread`) causes CPU thrashing and memory exhaustion. Thread pools maintain a fixed set of pre-allocated worker threads that process tasks from an internal queue efficiently.

In this activity, you will scale concurrent task execution using Python's `concurrent.futures.ThreadPoolExecutor`. You will implement `ThreadPoolFactory` to manage thread pool lifecycles and build `ExecutorAccountService` returning `Future` handles for all banking operations, demonstrating asynchronous task submission, result retrieval, and graceful shutdown.

Using thread pools decouples task submission from thread management, preventing system resource starvation under peak loads.

By the end of this activity, you will be able to: configure and manage `ThreadPoolExecutor` instances in Python, submit asynchronous tasks and handle `Future` results, and coordinate graceful thread pool shutdown.

## 3. Topic Coverage
- **Python concepts**
  - Thread pool management with `concurrent.futures.ThreadPoolExecutor`
  - Asynchronous handles with `concurrent.futures.Future`
  - Task submission via `executor.submit(fn, *args)`
- **Design patterns / architecture**
  - Thread Pool Pattern
  - Future / Promise Pattern
  - Graceful Resource Teardown Pattern
- **Domain concepts**
  - Asynchronous banking operations
  - Non-blocking task submission
  - Controlled worker concurrency

## 4. Steps to Run the Activity
1. Navigate to the activity directory:
   ```bash
   cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity29
   ```
2. Run the thread pool executor test suite:
   ```bash
   python gdb/tests/test_executor_service.py
   ```
3. Verify that concurrent tasks submit cleanly, futures resolve, and executor shuts down gracefully.

## 5. Target Files, Classes, Methods, Interfaces, Repos, Services

| Type | Name | Package | Status | Notes |
|------|------|---------|--------|-------|
| class | `ThreadPoolFactory` | `gdb.concurrency` | NEW | Factory creating configured `ThreadPoolExecutor` instances |
| service | `ExecutorAccountService` | `gdb.service` | NEW | Service submitting operations and returning `Future` handles |
| test | `test_executor_service.py` | `gdb.tests` | NEW | Verification test suite |

## 6. Step-by-Step Instructions of Implementation

### STEP 1: Implement ThreadPoolFactory
- **Where:** `gdb/concurrency/thread_pool_factory.py` — methods `new_fixed_pool(size)` and `shutdown(executor)`
- **What:** Create and return `concurrent.futures.ThreadPoolExecutor(max_workers=size)`. Implement `shutdown()` to call `executor.shutdown(wait=True)`.
- **Why:** Centralizes thread pool creation and teardown policies.
- **Hint:** Use `ThreadPoolExecutor(max_workers=size)`.

### STEP 2: Implement ExecutorAccountService
- **Where:** `gdb/service/executor_account_service.py`
- **What:** Wrap underlying `AccountService`. Implement `deposit_async()`, `withdraw_async()`, and `transfer_async()` by calling `self._executor.submit(...)` and returning the `Future`.
- **Why:** Converts synchronous blocking calls into non-blocking future handles.
- **Hint:** `return self._executor.submit(self._service.deposit, account_number, amount)`.

## 7. Acceptance Criteria
- [ ] `ThreadPoolFactory` instantiates properly sized `ThreadPoolExecutor` workers.
- [ ] `ExecutorAccountService` submits tasks without blocking the calling thread.
- [ ] Methods return `Future` objects resolving to the resulting `Transaction` or balance.
- [ ] 100 concurrent deposit tasks submitted to executor resolve with accurate final balance.
- [ ] `shutdown()` terminates worker threads gracefully without hanging.
- [ ] Running `test_executor_service.py` passes all test assertions.

## 8. Expected Output
```bash
$ python gdb/tests/test_executor_service.py
```
```text
============================================================
  ACTIVITY 29 — THREAD POOLS (EXECUTOR SERVICE & FUTURE) (PYTHON)
============================================================
[TEST 1] Submitting 100 Concurrent Deposit Tasks:
  All 100 deposit futures resolved successfully.
  Final Account Balance: Rs. 110000.0 (Expected: 110000.0)
  -> PASSED

[TEST 2] Graceful Executor Shutdown:
  Executor terminated cleanly.
  -> PASSED

============================================================
  🎉 ALL 2/2 ACTIVITY 29 EXECUTOR SERVICE TESTS PASSED!
============================================================
```

## 9. How to Run the Commands
```bash
# 1. Navigate to activity root
cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity29

# 2. Run test driver
python gdb/tests/test_executor_service.py
```
Verify success by confirming all 2 tests pass as described in Section 7.

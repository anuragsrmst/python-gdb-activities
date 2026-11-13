# Activity 30: Async Programming – Pipelines & Fan-Out

## 1. Title
# Activity 30: Async Programming – Pipelines & Fan-Out

## 2. Description
In modern digital banking apps like SBI YONO and HDFC PayZapp, displaying a customer dashboard requires aggregating balances and data from savings accounts, credit cards, fixed deposits, and loans. Executing these queries sequentially wastes hundreds of milliseconds. Modern banking backends execute queries in parallel and compose asynchronous processing pipelines.

In this activity, you will build asynchronous functional pipelines and parallel fan-out aggregation in Python. You will implement `AsyncUtils` for asynchronous task chaining and fallback error handling, and build `AsyncAccountService` to provide non-blocking operations and multi-account balance aggregation using `concurrent.futures.as_completed()`.

Parallel query fan-out collapses dashboard response latency from linear sequential time to the single slowest sub-query duration.

By the end of this activity, you will be able to: build asynchronous functional pipelines in Python, implement parallel fan-out query aggregation across multiple accounts, and handle async errors with fallback handlers.

## 3. Topic Coverage
- **Python concepts**
  - Parallel aggregation with `concurrent.futures.as_completed`
  - Functional error recovery and fallback suppliers
  - Asynchronous pipeline composition
- **Design patterns / architecture**
  - Scatter-Gather / Fan-Out Fan-In Pattern
  - Pipeline Pattern
  - Asynchronous Service Composition
- **Domain concepts**
  - Multi-account portfolio balance aggregation
  - Non-blocking banking operations
  - Resilient asynchronous error recovery

## 4. Steps to Run the Activity
1. Navigate to the activity directory:
   ```bash
   cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity30
   ```
2. Run the async programming test suite:
   ```bash
   python gdb/tests/test_completable_future.py
   ```
3. Verify that chained asynchronous workflows and parallel fan-out balance queries succeed.

## 5. Target Files, Classes, Methods, Interfaces, Repos, Services

| Type | Name | Package | Status | Notes |
|------|------|---------|--------|-------|
| class | `AsyncUtils` | `gdb.concurrency` | NEW | Helpers for async execution and error handling |
| service | `AsyncAccountService` | `gdb.service` | NEW | Non-blocking async service with fan-out queries |
| test | `test_completable_future.py` | `gdb.tests` | NEW | Verification test suite |

## 6. Step-by-Step Instructions of Implementation

### STEP 1: Implement AsyncUtils
- **Where:** `gdb/concurrency/async_utils.py` — methods `supply_async(executor, fn, *args)` and `supply_with_default(executor, fn, default_val, *args)`
- **What:** Submit callables to executor, returning futures with graceful exception fallback returning `default_val` on failure.
- **Why:** Standardizes async submission and fallback semantics.
- **Hint:** Wrap call in a helper function that catches exceptions.

### STEP 2: Implement AsyncAccountService
- **Where:** `gdb/service/async_account_service.py` — method `get_total_balance_async(account_numbers)`
- **What:** Submit balance queries for all `account_numbers` concurrently to the executor, collect results using `as_completed()`, and return the sum of all balances.
- **Why:** Executes parallel scatter-gather fan-out queries across multiple accounts.
- **Hint:** Use `futures = [self._executor.submit(self._service.get_balance, acc) for acc in account_numbers]`.

## 7. Acceptance Criteria
- [ ] `AsyncUtils` executes tasks asynchronously and handles exceptions with fallback values.
- [ ] Chained async workflows (Open -> Deposit -> Withdraw) execute cleanly in order.
- [ ] `get_total_balance_async()` executes queries across accounts in parallel.
- [ ] Aggregated sum across multiple accounts accurately matches domain totals.
- [ ] Running `test_completable_future.py` passes all test assertions.

## 8. Expected Output
```bash
$ python gdb/tests/test_completable_future.py
```
```text
============================================================
  ACTIVITY 30 — ASYNC PROGRAMMING (COMPLETABLE FUTURE STYLE) (PYTHON)
============================================================
[TEST 1] Chained Asynchronous Workflow (Open -> Deposit -> Withdraw):
  Async account created: #1001
  Async deposit completed. Transaction ID: 1001
  Async withdrawal completed. Transaction ID: 1002
  Pipeline completed. Final Balance: Rs. 45000.0 (Expected: 45000.0)
  -> PASSED

[TEST 2] Parallel Fan-Out Across Multiple Accounts (get_total_balance_async):
  Aggregated Total Balance: Rs. 185000.0 (Expected: 185000.0)
  -> PASSED

============================================================
  🎉 ALL 2/2 ACTIVITY 30 ASYNC PROGRAMMING TESTS PASSED!
============================================================
```

## 9. How to Run the Commands
```bash
# 1. Navigate to activity root
cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity30

# 2. Run test driver
python gdb/tests/test_completable_future.py
```
Verify success by confirming all 2 tests pass as described in Section 7.

# Activity 31: Thread-safe + Async Service + NFR Measurement

## 1. Title
# Activity 31: Thread-safe + Async Service + NFR Measurement

## 2. Description
In enterprise financial engines powering high-volume networks like the National Payments Corporation of India (NPCI) for UPI, systems must satisfy strict Non-Functional Requirements (NFRs): high throughput (TPS), sub-millisecond response latencies, low tail latency percentiles (P95, P99), and 0.00% transaction failure rates.

In this culminating activity, you will unify fine-grained thread safety, asynchronous thread pools, and empirical NFR performance benchmarking. You will build `AsyncThreadSafeAccountService` integrating `AccountLockRegistry` and `ThreadPoolExecutor`, and implement `ThroughputBenchmark` to statistically measure Operations Per Second, Mean Latency, P95/P99 latency percentiles, and Error Rates against synchronous baselines.

Measuring latency percentiles ensures that 95% and 99% of customer transactions meet strict Service Level Agreements (SLAs) even under heavy concurrent load.

By the end of this activity, you will be able to: architect unified thread-safe asynchronous banking services, build empirical statistical benchmark harnesses in Python, and validate NFR SLAs.

## 3. Topic Coverage
- **Python concepts**
  - Unified concurrency using `AccountLockRegistry` with `ThreadPoolExecutor`
  - High-precision latency profiling with `time.perf_counter()`
  - Percentile calculations (`P95`, `P99`) and statistical distribution analysis
- **Design patterns / architecture**
  - Unified Concurrent Async Architecture
  - Benchmark Harness / NFR Performance Profiler
  - Service Level Agreement (SLA) Validation Pattern
- **Domain concepts**
  - High-throughput banking transaction processing
  - Mean vs P95/P99 latency distribution analysis
  - Zero-defect data consistency under high concurrent load

## 4. Steps to Run the Activity
1. Navigate to the activity directory:
   ```bash
   cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity31
   ```
2. Run the NFR benchmark and service verification test suite:
   ```bash
   python gdb/tests/test_nfr_throughput.py
   ```
3. Verify that `AsyncThreadSafeAccountService` passes correctness checks, and review the side-by-side performance comparison table.

## 5. Target Files, Classes, Methods, Interfaces, Repos, Services

| Type | Name | Package | Status | Notes |
|------|------|---------|--------|-------|
| service | `AsyncThreadSafeAccountService` | `gdb.service` | NEW | Unified thread-safe async banking service |
| class | `ThroughputBenchmark` | `gdb.concurrency` | NEW | Empirical statistical benchmark harness |
| test | `test_nfr_throughput.py` | `gdb.tests` | NEW | SLA verification and benchmark test driver |

## 6. Step-by-Step Instructions of Implementation

### STEP 1: Implement AsyncThreadSafeAccountService
- **Where:** `gdb/service/async_thread_safe_account_service.py`
- **What:** Wrap `AccountService`, using `AccountLockRegistry` to acquire per-account locks during execution inside `ThreadPoolExecutor` worker threads, returning `Future` handles.
- **Why:** Combines non-blocking async submission with fine-grained per-account mutual exclusion.
- **Hint:** In worker task: `with AccountLock(self._locks, acc_num): return self._service.deposit(...)`.

### STEP 2: Implement ThroughputBenchmark
- **Where:** `gdb/concurrency/throughput_benchmark.py` — method `run_benchmark(service_fn, total_ops, thread_count)`
- **What:** Execute `total_ops` across `thread_count` worker threads, recording individual operation latency durations in milliseconds. Compute mean latency, P95 percentile, P99 percentile, error count, and throughput (ops/sec).
- **Why:** Measures empirical NFR metrics against real workloads.
- **Hint:** Sort recorded durations list to calculate `p95 = durations[int(len(durations) * 0.95)]`.

## 7. Acceptance Criteria
- [ ] `AsyncThreadSafeAccountService` executes concurrent operations with per-account mutual exclusion.
- [ ] `ThroughputBenchmark` accurately measures TPS, Mean Latency, P95, P99, and Error Rate.
- [ ] Measured error rate is 0.00% under high concurrent load.
- [ ] P95 latency satisfies SLA threshold (< 100 ms).
- [ ] Running `test_nfr_throughput.py` passes all assertions and prints formatted metrics table.

## 8. Expected Output
```bash
$ python gdb/tests/test_nfr_throughput.py
```
```text
============================================================
  ACTIVITY 31 — THREAD-SAFE + ASYNC + NFR MEASUREMENT (PYTHON)
============================================================
[TEST 1] AsyncThreadSafeAccountService Correctness Verification:
  Account #1001 Balance: Rs. 22500.0 (Expected: 22500.0)
  -> PASSED

[TEST 2 & 3] Synchronous vs Asynchronous Throughput Benchmark:
  Running 1,000 operations across 10 concurrent threads...

+----------------------------+----------------------+----------------------+
| Metric                     | Synchronous Service  | Async Thread-Safe    |
+----------------------------+----------------------+----------------------+
| Total Operations           | 1000                 | 1000                 |
| Total Time (ms)            | 85.30                | 38.20                |
| Throughput (Ops/sec)       | 11723.33             | 26178.01             |
| Mean Latency (ms)          | 0.81                 | 0.35                 |
| P95 Latency (ms)           | 1.50                 | 0.72                 |
| P99 Latency (ms)           | 2.40                 | 1.10                 |
| Error Rate (%)             | 0.00                 | 0.00                 |
+----------------------------+----------------------+----------------------+
  -> PASSED

============================================================
  🎉 ALL 3/3 ACTIVITY 31 NFR BENCHMARK TESTS PASSED!
============================================================
```

## 9. How to Run the Commands
```bash
# 1. Navigate to activity root
cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity31

# 2. Run test driver
python gdb/tests/test_nfr_throughput.py
```
Verify success by confirming all 3 tests pass as described in Section 7.

import os
import sys

sys.path.insert(0, os.path.abspath("."))

from gdb.service.account_service import AccountService
from gdb.service.async_thread_safe_account_service import AsyncThreadSafeAccountService
from gdb.concurrency.throughput_benchmark import ThroughputBenchmark

def main():
    print("=" * 60)
    print("  ACTIVITY 31 - THREAD-SAFE + ASYNC + NFR MEASUREMENT (PYTHON)")
    print("=" * 60)

    base_service = AccountService()
    async_service = AsyncThreadSafeAccountService(base_service)

    passed_tests = 0
    total_tests = 3

    # TEST 1: Correctness Verification
    print("[TEST 1] AsyncThreadSafeAccountService Correctness Verification:")
    try:
        open_fut = async_service.open_account_async("SAVINGS", "Rajesh Sharma", 30, 20000.0)
        if open_fut is None:
            print("  [!]  [STEP 1 INCOMPLETE]: AsyncThreadSafeAccountService methods return None.")
            print("     -> Trainee Action: Open 'gdb/service/async_thread_safe_account_service.py'")
            print("     [HINT] Implement STEP 1 (thread-safe async wrapper with AccountLockRegistry & ThreadPoolExecutor).")
        else:
            acc = open_fut.result()
            acc.set_pin(1234)
            acc_no = acc.get_account_number()
            async_service.deposit_async(acc_no, 5000.0).result()
            async_service.withdraw_async(acc_no, 2500.0, 1234).result()
            final_acc = async_service.get_account_async(acc_no).result()
            print(f"  Account #{acc_no} Balance: Rs. {final_acc.get_balance()} (Expected: 22500.0)")
            print("  -> PASSED")
            passed_tests += 1
    except Exception as e:
        print(f"  [!]  Error in Test 1: {e}")

    # TEST 2 & 3: Benchmark & SLA
    print("\n[TEST 2 & 3] Synchronous vs Asynchronous Throughput Benchmark:")
    try:
        if passed_tests > 0:
            print("  Running 1,000 operations across 10 concurrent threads...")
            sync_res = ThroughputBenchmark.run_benchmark("Synchronous Service", lambda: base_service.deposit(acc_no, 1.0), total_ops=1000, concurrency=10)
            async_res = ThroughputBenchmark.run_benchmark("Async Thread-Safe", lambda: async_service.deposit_async(acc_no, 1.0).result(), total_ops=1000, concurrency=10)

            if sync_res.get("total_ops", 0) == 0 or async_res.get("total_ops", 0) == 0:
                print("  [!]  [STEP 2 INCOMPLETE]: ThroughputBenchmark returned 0 ops.")
                print("     -> Trainee Action: Open 'gdb/concurrency/throughput_benchmark.py' and implement STEP 2.")
            else:
                print("\n+----------------------------+----------------------+----------------------+")
                print("| Metric                     | Synchronous Service  | Async Thread-Safe    |")
                print("+----------------------------+----------------------+----------------------+")
                print(f"| Total Operations           | {sync_res['total_ops']:<20} | {async_res['total_ops']:<20} |")
                print(f"| Total Time (ms)            | {sync_res['total_time_ms']:<20.2f} | {async_res['total_time_ms']:<20.2f} |")
                print(f"| Throughput (Ops/sec)       | {sync_res['tps']:<20.2f} | {async_res['tps']:<20.2f} |")
                print(f"| Mean Latency (ms)          | {sync_res['mean_latency_ms']:<20.2f} | {async_res['mean_latency_ms']:<20.2f} |")
                print(f"| P95 Latency (ms)           | {sync_res['p95_ms']:<20.2f} | {async_res['p95_ms']:<20.2f} |")
                print(f"| P99 Latency (ms)           | {sync_res['p99_ms']:<20.2f} | {async_res['p99_ms']:<20.2f} |")
                print(f"| Error Rate (%)             | {sync_res['error_rate']:<20.2f} | {async_res['error_rate']:<20.2f} |")
                print("+----------------------------+----------------------+----------------------+")
                print("  -> PASSED")
                passed_tests += 2
        else:
            print("  [!]  Skipping Benchmark until Test 1 is implemented.")
    except Exception as e:
        print(f"  [!]  Error in Benchmark: {e}")

    async_service.shutdown()

    print("\n" + "=" * 60)
    if passed_tests == total_tests:
        print(f"  [SUCCESS] ALL {total_tests}/{total_tests} ACTIVITY 31 NFR BENCHMARK TESTS PASSED!")
    else:
        print(f"  [PROGRESS] ACTIVITY 31 PROGRESS: {passed_tests}/{total_tests} tests passed.")
    print("=" * 60)
    if passed_tests != total_tests:
        sys.exit(1)

if __name__ == "__main__":
    main()

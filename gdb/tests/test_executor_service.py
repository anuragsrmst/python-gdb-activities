import os
import sys

sys.path.insert(0, os.path.abspath("."))

from gdb.service.account_service import AccountService
from gdb.service.executor_account_service import ExecutorAccountService

def main():
    print("=" * 60)
    print("  ACTIVITY 29 - THREAD POOLS (EXECUTOR SERVICE & FUTURE) (PYTHON)")
    print("=" * 60)

    base_service = AccountService()
    executor_service = ExecutorAccountService(base_service)
    acc = base_service.open_account("SAVINGS", "Rajesh Sharma", 30, 10000.0)
    acc_no = acc.get_account_number()

    passed_tests = 0
    total_tests = 2

    # TEST 1: Submitting 100 Concurrent Deposit Tasks
    print("[TEST 1] Submitting 100 Concurrent Deposit Tasks:")
    try:
        futures = [executor_service.deposit_async(acc_no, 1000.0) for _ in range(100)]
        if None in futures or len(futures) == 0:
            print("  [!]  [STEP 1-2 INCOMPLETE]: deposit_async() returned None instead of a Future.")
            print("     -> Trainee Action: Open 'gdb/concurrency/thread_pool_factory.py' (STEP 1)")
            print("     -> Trainee Action: Open 'gdb/service/executor_account_service.py' (STEP 2)")
            print("     [HINT] Implement ThreadPoolExecutor submission and return the Future object.")
        else:
            results = [f.result() for f in futures]
            final_bal = base_service.get_account(acc_no).get_balance()
            if final_bal != 110000.0:
                print(f"  [!]  Balance mismatch: {final_bal} != 110000.0")
            else:
                print(f"  All {len(results)} deposit futures resolved successfully.")
                print(f"  Final Account Balance: Rs. {final_bal} (Expected: 110000.0)")
                print("  -> PASSED")
                passed_tests += 1
    except Exception as e:
        print(f"  [!]  Error in Test 1: {e}")

    # TEST 2: Graceful Shutdown
    print("\n[TEST 2] Graceful Executor Shutdown:")
    try:
        executor_service.shutdown()
        print("  Executor terminated cleanly.")
        print("  -> PASSED")
        passed_tests += 1
    except Exception as e:
        print(f"  [!]  Error in Test 2: {e}")

    print("\n" + "=" * 60)
    if passed_tests == total_tests:
        print(f"  [SUCCESS] ALL {total_tests}/{total_tests} ACTIVITY 29 EXECUTOR SERVICE TESTS PASSED!")
    else:
        print(f"  [PROGRESS] ACTIVITY 29 PROGRESS: {passed_tests}/{total_tests} tests passed.")
    print("=" * 60)
    if passed_tests != total_tests:
        sys.exit(1)

if __name__ == "__main__":
    main()

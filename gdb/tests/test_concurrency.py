import os
import sys

sys.path.insert(0, os.path.abspath("."))

from gdb.service.thread_safe_account_service import ThreadSafeAccountService
from gdb.concurrency.concurrent_deposit_demo import ConcurrentDepositDemo

def main():
    print("=" * 60)
    print("  ACTIVITY 27 - CONCURRENCY & THREAD SAFETY TESTS (PYTHON)")
    print("=" * 60)

    service = ThreadSafeAccountService()
    acc = service.open_account("SAVINGS", "Rajesh Sharma", 30, 10000.0)
    acc_no = acc.get_account_number()

    # TEST 1: Concurrent Deposits to Same Account
    print("[TEST 1] Concurrent Deposits to Same Account:")
    threads = 10
    ops_per_thread = 100
    amount_per_op = 100.0
    expected_increase = threads * ops_per_thread * amount_per_op
    expected_balance = 10000.0 + expected_increase

    print(f"  Spawning {threads} threads, each making {ops_per_thread} deposits of Rs. {amount_per_op}...")
    final_balance = ConcurrentDepositDemo.run_demo(service, acc_no, threads, ops_per_thread, amount_per_op)

    print(f"  Initial Balance: Rs. 10000.0")
    print(f"  Expected Final Balance: Rs. {expected_balance}")
    print(f"  Actual Final Balance:   Rs. {final_balance}")

    if final_balance != expected_balance:
        print("\n  [!]  [STEP 1-2 INCOMPLETE]: Concurrent race condition or unstarted threads detected!")
        print("     -> Trainee Action: Open 'gdb/concurrency/concurrent_deposit_demo.py' (STEP 1)")
        print("     -> Trainee Action: Open 'gdb/service/thread_safe_account_service.py' (STEP 2)")
        print("     [HINT] Implement start_event barrier, spawn threads, and synchronize deposit() with RLock.")
        print("\n" + "=" * 60)
        print("  [PROGRESS] ACTIVITY 27 PROGRESS: 0/1 tests passed.")
        print("=" * 60)
        sys.exit(1)

    print("  -> PASSED (Zero lost updates!)")
    print("\n" + "=" * 60)
    print("  [SUCCESS] ALL ACTIVITY 27 CONCURRENCY TESTS PASSED! Excellent work!")
    print("=" * 60)

if __name__ == "__main__":
    main()

import os
import sys

sys.path.insert(0, os.path.abspath("."))

from gdb.service.account_service import AccountService
from gdb.service.async_account_service import AsyncAccountService

def main():
    print("=" * 60)
    print("  ACTIVITY 30 - ASYNC PROGRAMMING (COMPLETABLE FUTURE STYLE) (PYTHON)")
    print("=" * 60)

    base_service = AccountService()
    async_service = AsyncAccountService(base_service)

    passed_tests = 0
    total_tests = 2

    # TEST 1: Chained Asynchronous Workflow
    print("[TEST 1] Chained Asynchronous Workflow (Open -> Deposit -> Withdraw):")
    try:
        open_future = async_service.open_account_async("SAVINGS", "Rajesh Sharma", 30, 50000.0)
        if open_future is None:
            print("  [!]  [STEP 2 INCOMPLETE]: open_account_async() returned None.")
            print("     -> Trainee Action: Open 'gdb/service/async_account_service.py'")
            print("     [HINT] Implement STEP 2 by submitting methods to the executor and returning Future.")
        else:
            acc = open_future.result()
            acc.set_pin(1234)
            acc_no = acc.get_account_number()
            print(f"  Async account created: #{acc_no}")

            dep_future = async_service.deposit_async(acc_no, 10000.0)
            dep_txn = dep_future.result()
            print(f"  Async deposit completed. Transaction ID: {dep_txn.get_id()}")

            with_future = async_service.withdraw_async(acc_no, 15000.0, 1234)
            with_txn = with_future.result()
            print(f"  Async withdrawal completed. Transaction ID: {with_txn.get_id()}")

            final_bal = base_service.get_account(acc_no).get_balance()
            if final_bal != 45000.0:
                print(f"  [!]  Balance mismatch: {final_bal} != 45000.0")
            else:
                print(f"  Pipeline completed. Final Balance: Rs. {final_bal} (Expected: 45000.0)")
                print("  -> PASSED")
                passed_tests += 1
    except Exception as e:
        print(f"  [!]  Error in Test 1: {e}")

    # TEST 2: Parallel Fan-Out Across Multiple Accounts
    print("\n[TEST 2] Parallel Fan-Out Across Multiple Accounts (get_total_balance_async):")
    try:
        acc2 = base_service.open_account("CURRENT", "Priya Patel", 28, 40000.0)
        acc3 = base_service.open_account("SALARY", "Amit Kumar", 35, 100000.0)
        sum_future = async_service.get_total_balance_async([acc.get_account_number(), acc2.get_account_number(), acc3.get_account_number()])
        if sum_future is None:
            print("  [!]  [STEP 2 INCOMPLETE]: get_total_balance_async() returned None.")
            print("     -> Trainee Action: Implement get_total_balance_async() fan-out in async_account_service.py.")
        else:
            total = sum_future.result()
            if total != 185000.0:
                print(f"  [!]  Aggregated total mismatch: {total} != 185000.0")
            else:
                print(f"  Aggregated Total Balance: Rs. {total} (Expected: 185000.0)")
                print("  -> PASSED")
                passed_tests += 1
    except Exception as e:
        print(f"  [!]  Error in Test 2: {e}")

    async_service.shutdown()

    print("\n" + "=" * 60)
    if passed_tests == total_tests:
        print(f"  [SUCCESS] ALL {total_tests}/{total_tests} ACTIVITY 30 ASYNC PROGRAMMING TESTS PASSED!")
    else:
        print(f"  [PROGRESS] ACTIVITY 30 PROGRESS: {passed_tests}/{total_tests} tests passed.")
    print("=" * 60)
    if passed_tests != total_tests:
        sys.exit(1)

if __name__ == "__main__":
    main()

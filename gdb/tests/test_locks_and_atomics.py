import os
import sys
import threading

sys.path.insert(0, os.path.abspath("."))

from gdb.service.locked_account_service import LockedAccountService
from gdb.service.atomic_account_service import AtomicAccountService

def main():
    print("=" * 60)
    print("  ACTIVITY 28 - LOCKS, ATOMICS & CONCURRENT COLLECTIONS (PYTHON)")
    print("=" * 60)

    passed_tests = 0
    total_tests = 3

    # TEST 1: LockedAccountService Same Account
    print("[TEST 1] Fine-Grained Per-Account Locking (Same Account):")
    try:
        service = LockedAccountService()
        acc = service.open_account("SAVINGS", "Rajesh Sharma", 30, 10000.0)
        acc_no = acc.get_account_number()

        def deposit_worker():
            for _ in range(100):
                service.deposit(acc_no, 100.0)

        threads = [threading.Thread(target=deposit_worker) for _ in range(10)]
        for t in threads: t.start()
        for t in threads: t.join()

        final_bal = service.get_account(acc_no).get_balance()
        if final_bal != 110000.0:
            print(f"  [!]  [STEP 1-3 INCOMPLETE]: Final balance {final_bal} != 110000.0")
            print("     -> Trainee Action: Implement AccountLockRegistry (STEP 1) and LockedAccountService (STEP 3).")
        else:
            print(f"  Expected Balance: Rs. 110000.0, Actual: Rs. {final_bal}")
            print("  -> PASSED")
            passed_tests += 1
    except Exception as e:
        print(f"  [!]  Error in Test 1: {e}")

    # TEST 2: Deadlock-Free Bidirectional Transfers
    print("\n[TEST 2] Deadlock-Free Bidirectional Transfers:")
    try:
        acc1 = service.open_account("SAVINGS", "Alice", 30, 100000.0)
        acc2 = service.open_account("SAVINGS", "Bob", 30, 100000.0)
        acc1.set_pin(1234)
        acc2.set_pin(1234)
        acc1_no = acc1.get_account_number()
        acc2_no = acc2.get_account_number()

        def transfer_worker_1_to_2():
            for _ in range(50):
                service.transfer(acc1_no, acc2_no, 100.0, 1234)

        def transfer_worker_2_to_1():
            for _ in range(50):
                service.transfer(acc2_no, acc1_no, 100.0, 1234)

        t1 = threading.Thread(target=transfer_worker_1_to_2)
        t2 = threading.Thread(target=transfer_worker_2_to_1)
        t1.start(); t2.start()
        t1.join(); t2.join()

        total_bal = service.get_account(acc1_no).get_balance() + service.get_account(acc2_no).get_balance()
        if total_bal != 200000.0:
            print(f"  [!]  [STEP 3 INCOMPLETE]: Invariant balance corrupted: {total_bal}")
            print("     -> Trainee Action: Ensure ordered dual-locking (min/max account numbers) in LockedAccountService.")
        else:
            print(f"  Total Combined Balance Preserved: Rs. {total_bal}")
            print("  -> PASSED")
            passed_tests += 1
    except Exception as e:
        print(f"  [!]  Error in Test 2: {e}")

    # TEST 3: Atomic Sequence Counter
    print("\n[TEST 3] Lock-Free Atomic Sequence Counter:")
    try:
        atomic_service = AtomicAccountService()
        ids = set()
        lock = threading.Lock()

        def id_worker():
            for _ in range(100):
                nid = atomic_service.next_transaction_id()
                with lock:
                    ids.add(nid)

        threads = [threading.Thread(target=id_worker) for _ in range(10)]
        for t in threads: t.start()
        for t in threads: t.join()

        if len(ids) != 1000:
            print(f"  [!]  [STEP 4 INCOMPLETE]: Expected 1000 unique IDs, got {len(ids)}.")
            print("     -> Trainee Action: Open 'gdb/service/atomic_account_service.py' and implement STEP 4.")
        else:
            print(f"  Generated {len(ids)} unique transaction IDs concurrently.")
            print("  -> PASSED")
            passed_tests += 1
    except Exception as e:
        print(f"  [!]  Error in Test 3: {e}")

    print("\n" + "=" * 60)
    if passed_tests == total_tests:
        print(f"  [SUCCESS] ALL {total_tests}/{total_tests} ACTIVITY 28 TESTS PASSED!")
    else:
        print(f"  [PROGRESS] ACTIVITY 28 PROGRESS: {passed_tests}/{total_tests} tests passed.")
    print("=" * 60)
    if passed_tests != total_tests:
        sys.exit(1)

if __name__ == "__main__":
    main()

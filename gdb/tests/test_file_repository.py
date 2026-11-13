import os
import sys
import shutil

sys.path.insert(0, os.path.abspath("."))

from datetime import datetime
from gdb.domain.account_factory import AccountFactory
from gdb.domain.transaction import Transaction
from gdb.domain.transaction_type import TransactionType
from gdb.repository.file_account_repository import FileAccountRepository
from gdb.repository.file_transaction_repository import FileTransactionRepository

def main():
    print("=" * 60)
    print("  ACTIVITY 26 - FILE REPOSITORY (CSV + ATOMIC WRITES + BACKUP)")
    print("=" * 60)

    test_dir = "data_test"
    if os.path.exists(test_dir):
        try: shutil.rmtree(test_dir)
        except Exception: pass
    os.makedirs(test_dir, exist_ok=True)

    acc_file = os.path.join(test_dir, "accounts.csv")
    txn_file = os.path.join(test_dir, "transactions.csv")

    acc_repo = FileAccountRepository(acc_file, backup_enabled=True, max_backups=5)
    txn_repo = FileTransactionRepository(txn_file, backup_enabled=True, max_backups=5)

    passed_tests = 0
    total_tests = 4

    # TEST 1: Account Save & Read Back from CSV
    print("[TEST 1] Account Save & Read Back from CSV:")
    try:
        acc1 = AccountFactory.create_account("SAVINGS", 1001, "Rajesh Sharma", 30, 50000.0)
        acc1.set_pin(1234)
        acc_repo.save(acc1)
        found = acc_repo.find_by_id(1001)

        if found is None:
            print("  [!]  [STEP 1-4 INCOMPLETE]: Account #1001 was not persisted/loaded from CSV.")
            print("     -> Trainee Action: Complete STEP 1 (AtomicFileWriter), STEP 2 (CsvMapper), and STEP 4 (FileAccountRepository).")
        else:
            print(f"  Saved: {acc1.get_account_info()}")
            print(f"  Found: {found.get_account_info()}")
            print("  -> PASSED")
            passed_tests += 1
    except Exception as e:
        print(f"  [!]  Error in Test 1: {e}")

    # TEST 2: Multiple Accounts & Atomic Update
    print("\n[TEST 2] Multiple Accounts & Atomic Update:")
    try:
        if found is not None:
            acc2 = AccountFactory.create_account("CURRENT", 1002, "Priya Patel", 28, 40000.0)
            acc_repo.save(acc2)
            found.deposit(10000.0)
            acc_repo.update(found)
            updated = acc_repo.find_by_id(1001)
            if updated is None or updated.get_balance() != 60000.0:
                print("  [!]  [STEP 4 INCOMPLETE]: CSV update did not persist new balance.")
            else:
                print(f"  Updated balance: Rs. {updated.get_balance()} (Expected: 60000.0)")
                print("  -> PASSED")
                passed_tests += 1
        else:
            print("  [!]  Skipping Test 2 until Test 1 is implemented.")
    except Exception as e:
        print(f"  [!]  Error in Test 2: {e}")

    # TEST 3: Transaction Save & Query in CSV
    print("\n[TEST 3] Transaction Save & Query in CSV:")
    try:
        t1 = Transaction(201, datetime.now(), 1001, TransactionType.DEPOSIT, 10000.0, 60000.0, "SUCCESS", "Deposit", 0, 1001)
        txn_repo.save(t1)
        txns = txn_repo.find_by_account(1001)
        if len(txns) == 0:
            print("  [!]  [STEP 5 INCOMPLETE]: FileTransactionRepository not saving transactions.")
            print("     -> Trainee Action: Open 'gdb/repository/file_transaction_repository.py' and implement STEP 5.")
        else:
            print(f"  Found transactions for #1001: {len(txns)} (Expected: 1)")
            print("  -> PASSED")
            passed_tests += 1
    except Exception as e:
        print(f"  [!]  Error in Test 3: {e}")

    # TEST 4: Atomic Transfer via File Repository
    print("\n[TEST 4] Atomic Transfer via FileTransactionRepository:")
    try:
        if found is not None:
            txn_repo.transfer(1001, 1002, 5000.0)
            src_after = acc_repo.find_by_id(1001)
            dst_after = acc_repo.find_by_id(1002)
            if src_after is None or dst_after is None or src_after.get_balance() != 55000.0:
                print("  [!]  [STEP 5 INCOMPLETE]: File transfer did not update balances.")
            else:
                print(f"  Sender balance: Rs. {src_after.get_balance()} (Expected: 55000.0)")
                print(f"  Receiver balance: Rs. {dst_after.get_balance()} (Expected: 45000.0)")
                print("  -> PASSED")
                passed_tests += 1
        else:
            print("  [!]  Skipping Test 4 until previous tests are implemented.")
    except Exception as e:
        print(f"  [!]  Error in Test 4: {e}")

    if os.path.exists(test_dir):
        try: shutil.rmtree(test_dir)
        except Exception: pass

    print("\n" + "=" * 60)
    if passed_tests == total_tests:
        print(f"  [SUCCESS] ALL {total_tests}/{total_tests} ACTIVITY 26 FILE REPOSITORY TESTS PASSED!")
    else:
        print(f"  [PROGRESS] ACTIVITY 26 PROGRESS: {passed_tests}/{total_tests} tests passed.")
    print("=" * 60)
    if passed_tests != total_tests:
        sys.exit(1)

if __name__ == "__main__":
    main()

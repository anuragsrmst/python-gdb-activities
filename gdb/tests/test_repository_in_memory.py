import os
import sys

sys.path.insert(0, os.path.abspath("."))

from gdb.domain.account_factory import AccountFactory
from gdb.domain.transaction import Transaction
from gdb.domain.transaction_type import TransactionType
from gdb.repository.in_memory_account_repository import InMemoryAccountRepository
from gdb.repository.in_memory_transaction_repository import InMemoryTransactionRepository
from gdb.service.account_service import AccountService

def main():
    print("=" * 60)
    print("  ACTIVITY 21 - REPOSITORY PATTERN IN-MEMORY TESTS (PYTHON)")
    print("=" * 60)

    acc_repo = InMemoryAccountRepository()
    txn_repo = InMemoryTransactionRepository()
    passed_tests = 0
    total_tests = 3

    # TEST 1: Account Repository CRUD
    print("[TEST 1] Account Repository CRUD:")
    try:
        acc1 = AccountFactory.create_account("SAVINGS", 1001, "Rajesh Sharma", 30, 50000.0)
        acc1.set_pin(1234)
        acc_repo.save(acc1)
        found = acc_repo.find_by_id(1001)

        if found is None or found.get_account_number() != 1001:
            print("  [!]  [STEP 1-4 INCOMPLETE]: Account #1001 was not saved or found.")
            print("     -> Trainee Action: Open 'gdb/repository/in_memory_account_repository.py'")
            print("     [HINT] Implement STEP 1 (storage), STEP 2 (save), and STEP 3 (find_by_id).")
        else:
            print(f"  Saved: {found.get_account_info()}")
            found.deposit(15000.0)
            acc_repo.update(found)
            updated = acc_repo.find_by_id(1001)

            acc2 = AccountFactory.create_account("CURRENT", 1002, "Priya Patel", 28, 40000.0)
            acc_repo.save(acc2)
            all_accs = acc_repo.find_all()

            if updated.get_balance() != 65000.0 or len(all_accs) < 2:
                print("  [!]  [STEP 4-5 INCOMPLETE]: Update or find_all logic needs implementation.")
                print("     -> Trainee Action: Implement STEP 4 (find_all) and STEP 5 (update).")
            else:
                print(f"  Updated balance: Rs. {updated.get_balance()}")
                print(f"  Total accounts in repository: {len(all_accs)}")
                print("  -> PASSED")
                passed_tests += 1
    except Exception as e:
        print(f"  [!]  Error in Test 1: {e}")
        print("     -> Trainee Action: Check 'gdb/repository/in_memory_account_repository.py'")

    # TEST 2: Transaction Repository Operations
    print("\n[TEST 2] Transaction Repository Operations:")
    try:
        t1 = Transaction(101, None, 1001, TransactionType.DEPOSIT, 15000.0, 65000.0, "SUCCESS", "Deposit", 0, 1001)
        t2 = Transaction(102, None, 1001, TransactionType.TRANSFER, 5000.0, 60000.0, "SUCCESS", "Transfer", 1001, 1002)
        txn_repo.save(t1)
        txn_repo.save(t2)
        acc1_txns = txn_repo.find_by_account(1001)

        if len(acc1_txns) != 2:
            print(f"  [!]  [STEP 9-11 INCOMPLETE]: Expected 2 transactions, got {len(acc1_txns)}.")
            print("     -> Trainee Action: Open 'gdb/repository/in_memory_transaction_repository.py'")
            print("     [HINT] Implement STEP 9 (list), STEP 10 (save), and STEP 11 (find_by_account).")
        else:
            print(f"  Found transactions for #1001: {len(acc1_txns)}")
            print("  -> PASSED")
            passed_tests += 1
    except Exception as e:
        print(f"  [!]  Error in Test 2: {e}")
        print("     -> Trainee Action: Check 'gdb/repository/in_memory_transaction_repository.py'")

    # TEST 3: Service Integration with Repositories
    print("\n[TEST 3] Service Integration with Repositories:")
    try:
        service = AccountService(account_repository=acc_repo, transaction_repository=txn_repo)
        new_acc = service.open_account("SALARY", "Amit Kumar", 35, 20000.0)
        if new_acc is None:
            print("  [!]  [INCOMPLETE]: AccountService.open_account returned None.")
            print("     -> Trainee Action: Ensure repositories are properly injected and used.")
        else:
            print(f"  Opened account #{new_acc.get_account_number()} via AccountService.")
            txn = service.deposit(new_acc.get_account_number(), 5000.0)
            if new_acc.get_balance() != 25000.0:
                print(f"  [!]  Balance mismatch: {new_acc.get_balance()} != 25000.0")
            else:
                print(f"  Deposit executed. New Balance: Rs. {new_acc.get_balance()}")
                print("  -> PASSED")
                passed_tests += 1
    except Exception as e:
        print(f"  [!]  Error in Test 3: {e}")

    print("\n" + "=" * 60)
    if passed_tests == total_tests:
        print(f"  [SUCCESS] ALL {total_tests}/{total_tests} ACTIVITY 21 TESTS PASSED! Excellent work!")
    else:
        print(f"  [PROGRESS] ACTIVITY 21 PROGRESS: {passed_tests}/{total_tests} tests passed.")
        print("  [HINT] Follow the 📝 STEP instructions in your files to complete all tasks!")
    print("=" * 60)
    if passed_tests != total_tests:
        sys.exit(1)

if __name__ == "__main__":
    main()

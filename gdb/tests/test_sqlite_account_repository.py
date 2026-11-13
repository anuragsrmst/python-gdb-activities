import os
import sys

sys.path.insert(0, os.path.abspath("."))

from gdb.domain.account_factory import AccountFactory
from gdb.db.sqlite_connection_provider import SqliteConnectionProvider
from gdb.db.schema_initializer import SchemaInitializer
from gdb.repository.sqlite_account_repository import SqliteAccountRepository

def main():
    print("=" * 60)
    print("  ACTIVITY 23 - SQLITE ACCOUNT REPOSITORY CRUD TESTS")
    print("=" * 60)

    db_file = "test_acc_gdb.db"
    if os.path.exists(db_file):
        try: os.remove(db_file)
        except Exception: pass

    provider = SqliteConnectionProvider(db_file)
    SchemaInitializer.initialize(provider)
    repo = SqliteAccountRepository(provider)

    passed_tests = 0
    total_tests = 3

    # TEST 1: Save & FindById
    print("[TEST 1] Save & FindById:")
    try:
        acc1 = AccountFactory.create_account("SAVINGS", 1001, "Rajesh Sharma", 30, 50000.0)
        acc1.set_pin(1234)
        repo.save(acc1)
        found = repo.find_by_id(1001)

        if found is None:
            print("  [!]  [STEP 1-2 INCOMPLETE]: Account #1001 was not saved or retrieved from SQLite.")
            print("     -> Trainee Action: Open 'gdb/repository/sqlite_account_repository.py'")
            print("     [HINT] Implement STEP 1 (save INSERT query) and STEP 2 (find_by_id SELECT query).")
        else:
            print(f"  Found: {found.get_account_info()}")
            print("  -> PASSED")
            passed_tests += 1
    except Exception as e:
        print(f"  [!]  Error in Test 1: {e}")

    # TEST 2: Update & FindAll
    print("\n[TEST 2] Update & FindAll:")
    try:
        if found is not None:
            acc2 = AccountFactory.create_account("CURRENT", 1002, "Priya Patel", 28, 40000.0)
            repo.save(acc2)
            found.deposit(15000.0)
            repo.update(found)
            updated = repo.find_by_id(1001)
            all_accs = repo.find_all()

            if updated is None or updated.get_balance() != 65000.0 or len(all_accs) < 2:
                print("  [!]  [STEP 3-4 INCOMPLETE]: Update or find_all logic needs implementation.")
                print("     -> Trainee Action: Implement STEP 3 (find_all) and STEP 4 (update).")
            else:
                print(f"  Updated balance: Rs. {updated.get_balance()} (Expected: 65000.0)")
                print(f"  Total accounts in DB: {len(all_accs)} (Expected: 2)")
                print("  -> PASSED")
                passed_tests += 1
        else:
            print("  [!]  Skipping Test 2 until Test 1 is implemented.")
    except Exception as e:
        print(f"  [!]  Error in Test 2: {e}")

    # TEST 3: Delete & Exists
    print("\n[TEST 3] Delete & Exists:")
    try:
        if repo.exists(1002):
            repo.delete(1002)
            if not repo.exists(1002):
                print("  Account 1002 successfully deleted.")
                print("  -> PASSED")
                passed_tests += 1
            else:
                print("  [!]  [STEP 5-6 INCOMPLETE]: Account still exists after delete.")
                print("     -> Trainee Action: Implement STEP 5 (delete) and STEP 6 (exists).")
        else:
            print("  [!]  [STEP 6 INCOMPLETE]: exists() returned False.")
            print("     -> Trainee Action: Implement STEP 6 (exists SELECT query).")
    except Exception as e:
        print(f"  [!]  Error in Test 3: {e}")

    provider.close()
    if os.path.exists(db_file):
        try: os.remove(db_file)
        except Exception: pass

    print("\n" + "=" * 60)
    if passed_tests == total_tests:
        print(f"  [SUCCESS] ALL {total_tests}/{total_tests} ACTIVITY 23 SQLITE ACCOUNT REPOSITORY TESTS PASSED!")
    else:
        print(f"  [PROGRESS] ACTIVITY 23 PROGRESS: {passed_tests}/{total_tests} tests passed.")
        print("  [HINT] Complete the 📝 STEP placeholders in 'sqlite_account_repository.py'!")
    print("=" * 60)
    if passed_tests != total_tests:
        sys.exit(1)

if __name__ == "__main__":
    main()

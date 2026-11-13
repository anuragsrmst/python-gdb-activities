import os
import sys

sys.path.insert(0, os.path.abspath("."))

from datetime import datetime
from gdb.domain.account_factory import AccountFactory
from gdb.domain.transaction import Transaction
from gdb.domain.transaction_type import TransactionType
from gdb.db.sqlite_connection_provider import SqliteConnectionProvider
from gdb.db.schema_initializer import SchemaInitializer
from gdb.db.data_migrator import DataMigrator
from gdb.repository.sqlite_account_repository import SqliteAccountRepository
from gdb.repository.sqlite_transaction_repository import SqliteTransactionRepository
from gdb.repository.in_memory_account_repository import InMemoryAccountRepository
from gdb.repository.in_memory_transaction_repository import InMemoryTransactionRepository

def main():
    print("=" * 60)
    print("  ACTIVITY 24 - SQLITE TRANSACTION REPOSITORY & MIGRATION")
    print("=" * 60)

    db_file = "test_txn_gdb.db"
    if os.path.exists(db_file):
        try: os.remove(db_file)
        except Exception: pass

    provider = SqliteConnectionProvider(db_file)
    SchemaInitializer.initialize(provider)
    acc_repo = SqliteAccountRepository(provider)
    txn_repo = SqliteTransactionRepository(provider)

    passed_tests = 0
    total_tests = 3

    # Setup accounts
    acc1 = AccountFactory.create_account("SAVINGS", 1001, "Rajesh Sharma", 30, 50000.0)
    acc2 = AccountFactory.create_account("CURRENT", 1002, "Priya Patel", 28, 30000.0)
    acc_repo.save(acc1)
    acc_repo.save(acc2)

    # TEST 1: Transaction Save & Query
    print("[TEST 1] Transaction Save & Query:")
    try:
        t1 = Transaction(101, datetime.now(), 1001, TransactionType.DEPOSIT, 5000.0, 55000.0, "SUCCESS", "Deposit", 0, 1001)
        txn_repo.save(t1)
        txns = txn_repo.find_by_account(1001)
        if len(txns) == 0:
            print("  [!]  [STEP 1-2 INCOMPLETE]: No transactions found in SQLite database.")
            print("     -> Trainee Action: Open 'gdb/repository/sqlite_transaction_repository.py'")
            print("     [HINT] Implement STEP 1 (save transaction) and STEP 2 (find_by_account).")
        else:
            print(f"  Found transactions for #1001: {len(txns)}")
            print("  -> PASSED")
            passed_tests += 1
    except Exception as e:
        print(f"  [!]  Error in Test 1: {e}")

    # TEST 2: Atomic Transfer Execution
    print("\n[TEST 2] Atomic Transfer Execution:")
    try:
        txn_repo.transfer(1001, 1002, 10000.0)
        src_after = acc_repo.find_by_id(1001)
        dst_after = acc_repo.find_by_id(1002)
        if src_after is None or dst_after is None or src_after.get_balance() != 40000.0 or dst_after.get_balance() != 40000.0:
            print("  [!]  [STEP 4 INCOMPLETE]: Atomic transfer did not update balances correctly.")
            print("     -> Trainee Action: Open 'gdb/repository/sqlite_transaction_repository.py'")
            print("     [HINT] Implement STEP 4 (atomic multi-account transfer with commit/rollback).")
        else:
            print(f"  Updated Sender Balance: Rs. {src_after.get_balance()} (Expected: 40000.0)")
            print(f"  Updated Receiver Balance: Rs. {dst_after.get_balance()} (Expected: 40000.0)")
            print("  -> PASSED")
            passed_tests += 1
    except Exception as e:
        print(f"  [!]  Error in Test 2: {e}")

    # TEST 3: Data Migration from Memory to SQLite
    print("\n[TEST 3] Data Migration from Memory to SQLite:")
    try:
        mem_acc = InMemoryAccountRepository()
        mem_txn = InMemoryTransactionRepository()
        mem_acc.save(AccountFactory.create_account("SALARY", 1003, "Amit Kumar", 35, 75000.0))
        stats = DataMigrator.migrate(mem_acc, acc_repo, mem_txn, txn_repo)
        migrated_acc = acc_repo.find_by_id(1003)
        if migrated_acc is None or stats.get("accounts_migrated", 0) == 0:
            print("  [!]  [STEP 5 INCOMPLETE]: DataMigrator did not copy entities to SQLite.")
            print("     -> Trainee Action: Open 'gdb/db/data_migrator.py' and implement STEP 5.")
        else:
            print(f"  Migrated stats: {stats}")
            print("  -> PASSED")
            passed_tests += 1
    except Exception as e:
        print(f"  [!]  Error in Test 3: {e}")

    provider.close()
    if os.path.exists(db_file):
        try: os.remove(db_file)
        except Exception: pass

    print("\n" + "=" * 60)
    if passed_tests == total_tests:
        print(f"  [SUCCESS] ALL {total_tests}/{total_tests} ACTIVITY 24 TESTS PASSED! Excellent work!")
    else:
        print(f"  [PROGRESS] ACTIVITY 24 PROGRESS: {passed_tests}/{total_tests} tests passed.")
        print("  [HINT] Follow the 📝 STEP instructions in 'sqlite_transaction_repository.py'!")
    print("=" * 60)
    if passed_tests != total_tests:
        sys.exit(1)

if __name__ == "__main__":
    main()

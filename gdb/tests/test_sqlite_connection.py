import os
import sys

sys.path.insert(0, os.path.abspath("."))

from gdb.db.sqlite_connection_provider import SqliteConnectionProvider
from gdb.db.schema_initializer import SchemaInitializer

def main():
    print("=" * 60)
    print("  ACTIVITY 22 - SQLITE CONNECTION & SCHEMA INITIALIZATION")
    print("=" * 60)

    db_file = "test_conn_gdb.db"
    if os.path.exists(db_file):
        try: os.remove(db_file)
        except Exception: pass

    passed_tests = 0
    total_tests = 3

    # TEST 1: Database Connection Establishment
    print("[TEST 1] Database Connection Establishment:")
    try:
        provider = SqliteConnectionProvider(db_file)
        conn = provider.get_connection()
        if conn is None:
            print("  [!]  [STEP 1 INCOMPLETE]: Connection is None.")
            print("     -> Trainee Action: Open 'gdb/db/sqlite_connection_provider.py' and implement get_connection().")
        else:
            print(f"  Connected to: {db_file}")
            conn.close()
            print("  -> PASSED")
            passed_tests += 1
    except Exception as e:
        print(f"  [!]  Error in Test 1: {e}")

    # TEST 2 & 3: Schema DDL Execution & Verification
    print("\n[TEST 2 & 3] Schema DDL Execution & Verification:")
    try:
        SchemaInitializer.initialize(provider)
        conn = provider.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('accounts', 'transactions')")
        tables = [r["name"] for r in cursor.fetchall()]
        conn.close()

        if "accounts" not in tables or "transactions" not in tables:
            print(f"  [!]  [STEP 2 INCOMPLETE]: Tables missing! Found: {tables}")
            print("     -> Trainee Action: Open 'gdb/db/schema_initializer.py'")
            print("     [HINT] Implement STEP 2 by creating 'accounts' and 'transactions' tables.")
        else:
            print(f"  Verified tables in DB: {tables}")
            print("  -> PASSED (DDL initialized and verified)")
            passed_tests += 2
    except Exception as e:
        print(f"  [!]  Error in Schema DDL: {e}")
        print("     -> Trainee Action: Check 'gdb/db/schema_initializer.py'")

    if os.path.exists(db_file):
        try: os.remove(db_file)
        except Exception: pass

    print("\n" + "=" * 60)
    if passed_tests == total_tests:
        print(f"  [SUCCESS] ALL {total_tests}/{total_tests} ACTIVITY 22 TESTS PASSED! Great job!")
    else:
        print(f"  [PROGRESS] ACTIVITY 22 PROGRESS: {passed_tests}/{total_tests} tests passed.")
        print("  [HINT] Follow the 📝 STEP instructions in 'gdb/db/' to complete all tasks!")
    print("=" * 60)
    if passed_tests != total_tests:
        sys.exit(1)

if __name__ == "__main__":
    main()

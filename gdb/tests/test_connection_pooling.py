import os
import sys
import time

sys.path.insert(0, os.path.abspath("."))

from gdb.db.sqlite_connection_provider import SqliteConnectionProvider
from gdb.db.pooled_connection_provider import PooledConnectionProvider
from gdb.db.schema_initializer import SchemaInitializer

def main():
    print("=" * 60)
    print("  ACTIVITY 25 - CONNECTION POOLING BENCHMARK (PYTHON)")
    print("=" * 60)

    db_file = "test_pool_gdb.db"
    if os.path.exists(db_file):
        try: os.remove(db_file)
        except Exception: pass

    direct_provider = SqliteConnectionProvider(db_file)
    SchemaInitializer.initialize(direct_provider)

    passed_tests = 0
    total_tests = 2

    # TEST 1: Pool initialization & acquisition
    print("[TEST 1] Connection Pool Acquisition:")
    try:
        pooled_provider = PooledConnectionProvider(db_file, pool_size=10)
        conn = pooled_provider.get_connection()
        if conn is None:
            print("  [!]  [STEP 1-2 INCOMPLETE]: get_connection() returned None.")
            print("     -> Trainee Action: Open 'gdb/db/pooled_connection_provider.py'")
            print("     [HINT] Implement STEP 1 (pool queue) and STEP 2 (borrow connection).")
        else:
            pooled_provider.release_connection(conn)
            print("  Pooled connection successfully acquired and released.")
            print("  -> PASSED")
            passed_tests += 1
    except Exception as e:
        print(f"  [!]  Error in Test 1: {e}")

    # TEST 2: Latency Benchmark
    print("\n[TEST 2] Latency Benchmark (100 sequential connection cycles):")
    try:
        cycles = 100
        t0 = time.perf_counter()
        for _ in range(cycles):
            c = direct_provider.get_connection()
            c.close()
        unpooled_ms = (time.perf_counter() - t0) * 1000.0

        t0 = time.perf_counter()
        for _ in range(cycles):
            c = pooled_provider.get_connection()
            pooled_provider.release_connection(c)
        pooled_ms = (time.perf_counter() - t0) * 1000.0

        print(f"  Unpooled Direct Connections: {unpooled_ms:.2f} ms")
        print(f"  Pooled Connections:          {pooled_ms:.2f} ms")
        print("  -> PASSED")
        passed_tests += 1
    except Exception as e:
        print(f"  [!]  Error in Test 2: {e}")

    pooled_provider.close()
    direct_provider.close()
    if os.path.exists(db_file):
        try: os.remove(db_file)
        except Exception: pass

    print("\n" + "=" * 60)
    if passed_tests == total_tests:
        print(f"  [SUCCESS] ALL {total_tests}/{total_tests} ACTIVITY 25 CONNECTION POOLING TESTS PASSED!")
    else:
        print(f"  [PROGRESS] ACTIVITY 25 PROGRESS: {passed_tests}/{total_tests} tests passed.")
    print("=" * 60)
    if passed_tests != total_tests:
        sys.exit(1)

if __name__ == "__main__":
    main()

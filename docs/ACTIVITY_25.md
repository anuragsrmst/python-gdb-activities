# Activity 25: Connection Pooling Benchmark

## 1. Title
# Activity 25: Connection Pooling Benchmark

## 2. Description
In high-volume banking systems like HDFC Bank processing thousands of ATM and UPI transactions per second, opening and closing a physical database connection for every single query creates unacceptable latency overhead. Creating TCP sockets and authenticating connections takes substantial time and system resources.

In this activity, you will build a thread-safe connection pool in Python named `PooledConnectionProvider` using Python's synchronized `queue.Queue`. You will pre-populate a pool of reusable SQLite database connections and implement a latency benchmark comparing pooled connection reuse against raw unpooled connection establishment.

Reusing database connections drastically reduces per-operation response time and stabilizes database throughput under heavy multi-threaded loads.

By the end of this activity, you will be able to: design and implement a thread-safe connection pool in Python, measure and compare connection establishment latency, and manage pooled resource lifecycles cleanly.

## 3. Topic Coverage
- **Python concepts**
  - Thread-safe queues with `queue.Queue`
  - High-precision latency timing with `time.perf_counter()`
  - Synchronized resource acquisition and release
- **Design patterns / architecture**
  - Object Pool Pattern
  - Connection Provider Pattern
  - Micro-benchmarking and performance profiling
- **Domain concepts**
  - Database connection lifecycle management
  - Throughput optimization in financial engines
  - Connection starvation and timeout handling

## 4. Steps to Run the Activity
1. Navigate to the activity directory:
   ```bash
   cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity25
   ```
2. Run the connection pooling benchmark test:
   ```bash
   python gdb/tests/test_connection_pooling.py
   ```
3. Verify that pooled connection acquisition succeeds and that the pooled benchmark demonstrates lower latency.

## 5. Target Files, Classes, Methods, Interfaces, Repos, Services

| Type | Name | Package | Status | Notes |
|------|------|---------|--------|-------|
| interface | `ConnectionProvider` | `gdb.db` | PROVIDED | Base connection provider interface |
| class | `PooledConnectionProvider` | `gdb.db` | NEW | Thread-safe connection pool using `queue.Queue` |
| test | `test_connection_pooling.py` | `gdb.tests` | NEW | Latency benchmark and verification test suite |

## 6. Step-by-Step Instructions of Implementation

### STEP 1: Initialize Connection Pool
- **Where:** `gdb/db/pooled_connection_provider.py` — method `__init__(db_path, pool_size=10)`
- **What:** Initialize `self._pool = queue.Queue(maxsize=pool_size)` and pre-create `pool_size` open SQLite connection instances configured with `conn.row_factory = sqlite3.Row`.
- **Why:** Pre-allocates connections during application startup.
- **Hint:** Use a loop: `for _ in range(pool_size): conn = sqlite3.connect(...); self._pool.put(conn)`.

### STEP 2: Implement get_connection()
- **Where:** `gdb/db/pooled_connection_provider.py` — method `get_connection(timeout=5.0)`
- **What:** Acquire and return an available connection from `self._pool.get(timeout=timeout)`.
- **Why:** Provides fast, non-blocking connection retrieval for worker threads.
- **Hint:** Raise an exception if `queue.Empty` is encountered after the timeout.

### STEP 3: Implement release_connection(conn)
- **Where:** `gdb/db/pooled_connection_provider.py` — method `release_connection(conn)`
- **What:** Return the connection to `self._pool.put(conn)`.
- **Why:** Reclaims active connections for subsequent operations.
- **Hint:** Catch `queue.Full` defensively or ensure pool size invariants.

### STEP 4: Implement close()
- **Where:** `gdb/db/pooled_connection_provider.py` — method `close()`
- **What:** Drain all connections from `self._pool` and call `conn.close()` on each.
- **Why:** Ensures clean shutdown and releases operating system file handles.
- **Hint:** While queue is not empty, call `get()` then `close()`.

## 7. Acceptance Criteria
- [ ] `PooledConnectionProvider` pre-populates `pool_size` open SQLite connections.
- [ ] `get_connection()` returns an available connection from the pool.
- [ ] `release_connection()` returns the connection back to the pool without closing it.
- [ ] `close()` cleanly closes all pooled connections upon application shutdown.
- [ ] Connection pooling benchmark demonstrates reduced latency compared to unpooled connections.
- [ ] Running `test_connection_pooling.py` completes with all assertions passing.

## 8. Expected Output
```bash
$ python gdb/tests/test_connection_pooling.py
```
```text
============================================================
  ACTIVITY 25 — CONNECTION POOLING BENCHMARK (PYTHON)
============================================================
[TEST 1] Connection Pool Acquisition:
  Pooled connection successfully acquired and released.
  -> PASSED

[TEST 2] Latency Benchmark (100 sequential connection cycles):
  Unpooled Direct Connections: 20.96 ms
  Pooled Connections:          13.10 ms
  -> PASSED

============================================================
  🎉 ALL 2/2 ACTIVITY 25 CONNECTION POOLING TESTS PASSED!
============================================================
```

## 9. How to Run the Commands
```bash
# 1. Navigate to activity root
cd c:\Users\DELL\Downloads\gdb-Activities\trainee_multi-lang-activities\python-gdb-activities\activity25

# 2. Run test driver
python gdb/tests/test_connection_pooling.py

# 3. Clean up test database
rm -f test_pool.db
```
Verify success by confirming all 2 tests pass as described in Section 7.

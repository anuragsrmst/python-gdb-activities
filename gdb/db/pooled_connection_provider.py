import sqlite3
import queue
from gdb.db.connection_provider import ConnectionProvider

class PooledConnectionProvider(ConnectionProvider):
    def __init__(self, db_path: str = "gdb_bank.db", pool_size: int = 10):
        # 📝 STEP 1: Pre-allocate connections in queue.Queue(maxsize=pool_size)
        self.db_path = db_path
        self.pool_size = pool_size
        self._pool = queue.Queue(maxsize=pool_size)

    def get_connection(self) -> sqlite3.Connection:
        # 📝 STEP 2: Borrow connection from pool
        return None

    def release_connection(self, conn: sqlite3.Connection) -> None:
        # 📝 STEP 3: Return connection back to pool
        pass

    def close(self) -> None:
        pass

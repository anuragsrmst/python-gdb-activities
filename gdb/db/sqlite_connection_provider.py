import sqlite3
from typing import Optional
from gdb.db.connection_provider import ConnectionProvider

class SqliteConnectionProvider(ConnectionProvider):
    def __init__(self, db_path: str = "gdb_bank.db"):
        self.db_path = db_path
        self._closed = False

    def get_connection(self) -> sqlite3.Connection:
        # 📝 STEP 1: Connect to sqlite database and set row_factory to sqlite3.Row
        return None

    def close(self) -> None:
        self._closed = True

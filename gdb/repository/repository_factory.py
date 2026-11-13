import os
from gdb.repository.account_repository import AccountRepository
from gdb.repository.transaction_repository import TransactionRepository
from gdb.repository.in_memory_account_repository import InMemoryAccountRepository
from gdb.repository.in_memory_transaction_repository import InMemoryTransactionRepository

class RepositoryFactory:
    _account_repository = None
    _transaction_repository = None
    _connection_provider = None

    @classmethod
    def get_account_repository(cls) -> AccountRepository:
        mode = os.environ.get("PERSISTENCE_MODE", "memory").lower()
        if mode == "sqlite":
            from gdb.repository.sqlite_account_repository import SqliteAccountRepository
            if cls._account_repository is None or not isinstance(cls._account_repository, SqliteAccountRepository):
                cls._account_repository = SqliteAccountRepository(cls.get_connection_provider())
            return cls._account_repository
        elif mode == "file":
            from gdb.repository.file_account_repository import FileAccountRepository
            if cls._account_repository is None or not isinstance(cls._account_repository, FileAccountRepository):
                cls._account_repository = FileAccountRepository("data/accounts.csv")
            return cls._account_repository
        else:
            if cls._account_repository is None:
                cls._account_repository = InMemoryAccountRepository()
            return cls._account_repository

    @classmethod
    def get_transaction_repository(cls) -> TransactionRepository:
        mode = os.environ.get("PERSISTENCE_MODE", "memory").lower()
        if mode == "sqlite":
            from gdb.repository.sqlite_transaction_repository import SqliteTransactionRepository
            if cls._transaction_repository is None or not isinstance(cls._transaction_repository, SqliteTransactionRepository):
                cls._transaction_repository = SqliteTransactionRepository(cls.get_connection_provider())
            return cls._transaction_repository
        elif mode == "file":
            from gdb.repository.file_transaction_repository import FileTransactionRepository
            if cls._transaction_repository is None or not isinstance(cls._transaction_repository, FileTransactionRepository):
                cls._transaction_repository = FileTransactionRepository("data/transactions.csv")
            return cls._transaction_repository
        else:
            if cls._transaction_repository is None:
                cls._transaction_repository = InMemoryTransactionRepository()
            return cls._transaction_repository

    @classmethod
    def get_connection_provider(cls):
        if cls._connection_provider is None:
            pool_enabled = os.environ.get("DB_POOL_ENABLED", "false").lower() == "true"
            if pool_enabled:
                from gdb.db.pooled_connection_provider import PooledConnectionProvider
                cls._connection_provider = PooledConnectionProvider("gdb_bank.db", pool_size=10)
            else:
                from gdb.db.sqlite_connection_provider import SqliteConnectionProvider
                cls._connection_provider = SqliteConnectionProvider("gdb_bank.db")
        return cls._connection_provider

    @classmethod
    def reset(cls):
        cls._account_repository = None
        cls._transaction_repository = None
        cls._connection_provider = None

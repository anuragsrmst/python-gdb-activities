# gdb/repository/sqlite_account_repository.py
import sqlite3
from typing import List, Optional
from gdb.domain.iaccount import IAccount
from gdb.domain.account_factory import AccountFactory
from gdb.db.connection_provider import ConnectionProvider
from gdb.repository.account_repository import AccountRepository

class SqliteAccountRepository(AccountRepository):
    """
    Relational SQLite implementation of AccountRepository for single-entity CRUD operations.
    """

    def __init__(self, provider: ConnectionProvider):
        self.provider = provider

    # ============================================================
    # 📝 STEP 1: Implement save(account)
    #
    # INSTRUCTIONS:
    #   1. Acquire connection from self.provider.get_connection().
    #   2. Execute parameterized INSERT INTO accounts query with values:
    #      (account_number, holder_name, age, balance, account_type, status, pin, opening_date, 0.0, 0.0)
    #   3. Commit transaction and close connection in a finally block.
    # ============================================================
    def save(self, account: IAccount) -> None:
        # TODO: Parameterized INSERT query for account
        pass

    # ============================================================
    # 📝 STEP 2: Implement find_by_id(account_number)
    #
    # INSTRUCTIONS:
    #   1. Acquire connection and execute SELECT * FROM accounts WHERE account_number = ?
    #   2. Fetch row and map using self._map_row(row).
    #   3. Return mapped IAccount or None if not found. Close connection in finally.
    # ============================================================
    def find_by_id(self, account_number: int) -> Optional[IAccount]:
        # TODO: Parameterized SELECT query by account_number
        return None

    # ============================================================
    # 📝 STEP 3: Implement find_all()
    #
    # INSTRUCTIONS:
    #   1. Acquire connection and execute SELECT * FROM accounts.
    #   2. Map all rows to a list of IAccount.
    #   3. Close connection in finally block.
    # ============================================================
    def find_all(self) -> List[IAccount]:
        # TODO: Parameterized SELECT query returning all accounts
        return []

    # ============================================================
    # 📝 STEP 4: Implement update(account)
    #
    # INSTRUCTIONS:
    #   1. Acquire connection from provider.
    #   2. Execute parameterized UPDATE accounts SET balance=?, status=? WHERE account_number=?
    #   3. Commit transaction and close connection in finally block.
    # ============================================================
    def update(self, account: IAccount) -> None:
        # TODO: Parameterized UPDATE query for account
        pass

    # ============================================================
    # 📝 STEP 5: Implement delete(account_number)
    #
    # INSTRUCTIONS:
    #   1. Acquire connection from provider.
    #   2. Execute parameterized DELETE FROM accounts WHERE account_number = ?
    #   3. Commit transaction and close connection in finally block.
    # ============================================================
    def delete(self, account_number: int) -> None:
        # TODO: Parameterized DELETE query by account_number
        pass

    # ============================================================
    # 📝 STEP 6: Implement exists(account_number)
    #
    # INSTRUCTIONS:
    #   1. Execute SELECT 1 FROM accounts WHERE account_number = ?
    #   2. Return True if cursor.fetchone() is not None, else False.
    # ============================================================
    def exists(self, account_number: int) -> bool:
        # TODO: Parameterized SELECT 1 query for existence
        return False

    # ============================================================
    # 📝 STEP 7: Implement next_account_number()
    #
    # INSTRUCTIONS:
    #   1. Execute SELECT COALESCE(MAX(account_number), 1000) + 1 FROM accounts
    #   2. Return integer result.
    # ============================================================
    def next_account_number(self) -> int:
        # TODO: Query database for next account number
        return 1001

    def _map_row(self, row) -> IAccount:
        acc_type = row["account_type"].upper()
        acc = AccountFactory.create_account(
            acc_type,
            row["account_number"],
            row["account_holder_name"],
            row["age"],
            row["balance"]
        )
        if row["pin"]:
            acc.set_pin(row["pin"])
        if row["status"] == "Inactive":
            acc.close()
        return acc

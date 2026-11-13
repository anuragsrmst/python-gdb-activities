# gdb/repository/sqlite_transaction_repository.py
import sqlite3
from datetime import datetime
from typing import List
from gdb.domain.transaction import Transaction
from gdb.domain.transaction_type import TransactionType
from gdb.db.connection_provider import ConnectionProvider
from gdb.repository.transaction_repository import TransactionRepository

class SqliteTransactionRepository(TransactionRepository):
    """
    Relational SQLite implementation of TransactionRepository for ledger persistence and atomic transfers.
    """

    def __init__(self, provider: ConnectionProvider):
        self.provider = provider

    # ============================================================
    # 📝 STEP 1: Implement save(transaction)
    #
    # INSTRUCTIONS:
    #   1. Acquire connection from provider.
    #   2. Execute parameterized INSERT INTO transactions query with values.
    #   3. Commit and close connection in finally block.
    # ============================================================
    def save(self, transaction: Transaction) -> None:
        # TODO: Insert transaction record into database
        pass

    # ============================================================
    # 📝 STEP 2: Implement find_by_account(account_number)
    #
    # INSTRUCTIONS:
    #   1. Execute: SELECT * FROM transactions WHERE account_number = ? OR from_account = ? OR to_account = ? ORDER BY transaction_id ASC
    #   2. Map rows to Transaction domain objects and return list.
    # ============================================================
    def find_by_account(self, account_number: int) -> List[Transaction]:
        # TODO: Query transactions where account_number matches
        return []

    # ============================================================
    # 📝 STEP 3: Implement find_all()
    #
    # INSTRUCTIONS:
    #   1. Execute: SELECT * FROM transactions ORDER BY transaction_id ASC
    #   2. Map all rows to a list of Transaction domain objects.
    # ============================================================
    def find_all(self) -> List[Transaction]:
        # TODO: Query all transactions from database
        return []

    def clear(self) -> None:
        conn = self.provider.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM transactions")
            conn.commit()
        finally:
            conn.close()

    # ============================================================
    # 📝 STEP 4: Implement transfer(from_account, to_account, amount)
    #
    # INSTRUCTIONS:
    #   1. Acquire connection and execute debit and credit updates atomically.
    #   2. Debit: UPDATE accounts SET balance = balance - ? WHERE account_number = ?
    #   3. Credit: UPDATE accounts SET balance = balance + ? WHERE account_number = ?
    #   4. Insert audit record into transactions table.
    #   5. Call conn.commit(). In case of error, call conn.rollback() and re-raise.
    # ============================================================
    def transfer(self, from_account_number: int, to_account_number: int, amount: float) -> None:
        # TODO: Atomically debit from_account, credit to_account, and insert audit row
        pass

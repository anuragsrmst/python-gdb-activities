# gdb/repository/in_memory_transaction_repository.py
from typing import List
import threading
from gdb.domain.transaction import Transaction
from gdb.repository.transaction_repository import TransactionRepository

class InMemoryTransactionRepository(TransactionRepository):
    """
    Thread-safe in-memory repository for Transaction audit ledgers.
    """

    # ============================================================
    # 📝 STEP 9: Initialize Transaction Storage & Lock
    #
    # INSTRUCTIONS:
    #   1. Initialize an empty list self._transactions: List[Transaction] = []
    #   2. Initialize a re-entrant lock self._lock = threading.RLock()
    # ============================================================
    def __init__(self):
        # TODO: Initialize transaction list storage and lock
        self._transactions: List[Transaction] = []
        self._lock = threading.RLock()

    # ============================================================
    # 📝 STEP 10: Implement save(transaction)
    #
    # INSTRUCTIONS:
    #   1. Acquire self._lock.
    #   2. Append transaction to self._transactions.
    # ============================================================
    def save(self, transaction: Transaction) -> None:
        # TODO: Save transaction record under lock
        pass

    # ============================================================
    # 📝 STEP 11: Implement find_by_account(account_number)
    #
    # INSTRUCTIONS:
    #   1. Acquire self._lock.
    #   2. Return all transactions where account_number matches primary, from, or to account.
    # ============================================================
    def find_by_account(self, account_number: int) -> List[Transaction]:
        # TODO: Return filtered transactions for account_number
        return []

    # ============================================================
    # 📝 STEP 12: Implement find_all()
    #
    # INSTRUCTIONS:
    #   1. Acquire self._lock.
    #   2. Return a shallow copy list of all stored transactions.
    # ============================================================
    def find_all(self) -> List[Transaction]:
        # TODO: Return list of all transactions
        return []

    def clear(self) -> None:
        with self._lock:
            self._transactions.clear()

    # ============================================================
    # 📝 STEP 14: Implement transfer(from_account, to_account, amount)
    #
    # INSTRUCTIONS:
    #   1. Record transfer transaction between accounts.
    # ============================================================
    def transfer(self, from_account_number: int, to_account_number: int, amount: float) -> None:
        # TODO: Record transfer transaction in audit ledger
        pass

# gdb/repository/in_memory_account_repository.py
from typing import List, Optional, Dict
import threading
from gdb.domain.iaccount import IAccount
from gdb.repository.account_repository import AccountRepository

class InMemoryAccountRepository(AccountRepository):
    """
    Thread-safe in-memory repository implementation for Account entities using RLock.
    """

    # ============================================================
    # 📝 STEP 1: Initialize In-Memory Storage & Lock
    #
    # INSTRUCTIONS:
    #   1. Initialize an empty dictionary self._storage: Dict[int, IAccount] = {}
    #   2. Initialize a re-entrant lock self._lock = threading.RLock()
    #   3. Initialize sequence counter self._next_id = 1001
    # ============================================================
    def __init__(self):
        # TODO: Initialize dictionary storage, lock, and sequence counter
        self._storage: Dict[int, IAccount] = {}
        self._lock = threading.RLock()
        self._next_id = 1001

    # ============================================================
    # 📝 STEP 2: Implement save(account)
    #
    # INSTRUCTIONS:
    #   1. Acquire self._lock.
    #   2. Store account in self._storage using its account number as key.
    # ============================================================
    def save(self, account: IAccount) -> None:
        # TODO: Save account into storage under lock
        pass

    # ============================================================
    # 📝 STEP 3: Implement find_by_id(account_number)
    #
    # INSTRUCTIONS:
    #   1. Acquire self._lock.
    #   2. Return the account matching account_number, or None if absent.
    # ============================================================
    def find_by_id(self, account_number: int) -> Optional[IAccount]:
        # TODO: Retrieve and return account by account_number
        return None

    # ============================================================
    # 📝 STEP 4: Implement find_all()
    #
    # INSTRUCTIONS:
    #   1. Acquire self._lock.
    #   2. Return a shallow copy list of all accounts in self._storage.values().
    # ============================================================
    def find_all(self) -> List[IAccount]:
        # TODO: Return list of all stored accounts
        return []

    # ============================================================
    # 📝 STEP 5: Implement update(account)
    #
    # INSTRUCTIONS:
    #   1. Acquire self._lock.
    #   2. If account exists in self._storage, update its entry; otherwise ignore.
    # ============================================================
    def update(self, account: IAccount) -> None:
        # TODO: Update existing account entry under lock
        pass

    # ============================================================
    # 📝 STEP 6: Implement delete(account_number)
    #
    # INSTRUCTIONS:
    #   1. Acquire self._lock.
    #   2. Remove entry with account_number from self._storage if present.
    # ============================================================
    def delete(self, account_number: int) -> None:
        # TODO: Delete account by account_number
        pass

    # ============================================================
    # 📝 STEP 7: Implement exists(account_number)
    #
    # INSTRUCTIONS:
    #   1. Acquire self._lock.
    #   2. Return True if account_number exists in self._storage, else False.
    # ============================================================
    def exists(self, account_number: int) -> bool:
        # TODO: Check existence of account_number
        return False

    # ============================================================
    # 📝 STEP 8: Implement next_account_number()
    #
    # INSTRUCTIONS:
    #   1. Acquire self._lock.
    #   2. Atomically increment self._next_id and return the generated number.
    # ============================================================
    def next_account_number(self) -> int:
        # TODO: Generate and return next unique account number
        return 1001

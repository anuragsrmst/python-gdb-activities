import threading
from typing import Dict

class AccountLockRegistry:
    def __init__(self):
        # 📝 STEP 1: Initialize dictionary for per-account locks
        self._locks: Dict[int, threading.RLock] = {}
        self._reg_lock = threading.RLock()

    def get_lock(self, account_number: int) -> threading.RLock:
        # 📝 STEP 1: Return or create RLock for specific account_number
        with self._reg_lock:
            if account_number not in self._locks:
                self._locks[account_number] = threading.RLock()
            return self._locks[account_number]

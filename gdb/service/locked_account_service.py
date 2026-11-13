from gdb.service.account_service import AccountService
from gdb.concurrency.account_lock_registry import AccountLockRegistry
from gdb.concurrency.account_lock import AccountLock

class LockedAccountService(AccountService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 📝 STEP 3: Initialize AccountLockRegistry
        self._lock_registry = AccountLockRegistry()

    def deposit(self, account_number: int, amount: float):
        # 📝 STEP 3: Lock only the target account during deposit
        with AccountLock(self._lock_registry.get_lock(account_number)):
            return super().deposit(account_number, amount)

    def withdraw(self, account_number: int, amount: float, pin: int):
        # 📝 STEP 3: Lock only the target account during withdraw
        with AccountLock(self._lock_registry.get_lock(account_number)):
            return super().withdraw(account_number, amount, pin)

    def transfer(self, from_account_number: int, to_account_number: int, amount: float, pin: int):
        # 📝 STEP 3: Acquire locks in numerical order to prevent deadlocks
        first = min(from_account_number, to_account_number)
        second = max(from_account_number, to_account_number)
        with AccountLock(self._lock_registry.get_lock(first)):
            with AccountLock(self._lock_registry.get_lock(second)):
                return super().transfer(from_account_number, to_account_number, amount, pin)

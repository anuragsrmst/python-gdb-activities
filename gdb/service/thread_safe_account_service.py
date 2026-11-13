import threading
from gdb.service.account_service import AccountService

class ThreadSafeAccountService(AccountService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 📝 STEP 2: Initialize RLock for synchronization
        self._sync_lock = threading.RLock()

    def deposit(self, account_number: int, amount: float):
        # 📝 STEP 2: Synchronize deposit under lock
        return super().deposit(account_number, amount)

    def withdraw(self, account_number: int, amount: float, pin: int):
        # 📝 STEP 2: Synchronize withdraw under lock
        return super().withdraw(account_number, amount, pin)

    def transfer(self, from_account_number: int, to_account_number: int, amount: float, pin: int):
        # 📝 STEP 2: Synchronize transfer under lock
        return super().transfer(from_account_number, to_account_number, amount, pin)

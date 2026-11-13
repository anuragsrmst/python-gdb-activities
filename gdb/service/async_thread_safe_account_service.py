from concurrent.futures import ThreadPoolExecutor, Future
from gdb.service.account_service import AccountService
from gdb.concurrency.account_lock_registry import AccountLockRegistry
from gdb.concurrency.account_lock import AccountLock

class AsyncThreadSafeAccountService:
    def __init__(self, service: AccountService, executor: ThreadPoolExecutor = None):
        # 📝 STEP 1: Initialize service, lock registry, and executor
        self._service = service
        self._locks = AccountLockRegistry()
        self._executor = executor or ThreadPoolExecutor(max_workers=10)

    def open_account_async(self, account_type: str, holder_name: str, age: int, initial_deposit: float) -> Future:
        # 📝 STEP 1: Return Future for open_account
        return None

    def deposit_async(self, account_number: int, amount: float) -> Future:
        # 📝 STEP 1: Return Future acquiring account lock during execution
        return None

    def withdraw_async(self, account_number: int, amount: float, pin: int) -> Future:
        # 📝 STEP 1: Return Future acquiring account lock during execution
        return None

    def transfer_async(self, from_account_number: int, to_account_number: int, amount: float, pin: int) -> Future:
        # 📝 STEP 1: Return Future acquiring dual ordered locks during execution
        return None

    def get_account_async(self, account_number: int) -> Future:
        # 📝 STEP 1: Return Future retrieving account under lock
        return None

    def shutdown(self) -> None:
        if self._executor:
            self._executor.shutdown(wait=True)

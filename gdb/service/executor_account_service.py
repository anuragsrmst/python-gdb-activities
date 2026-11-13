from concurrent.futures import ThreadPoolExecutor, Future
from gdb.service.account_service import AccountService
from gdb.concurrency.thread_pool_factory import ThreadPoolFactory

class ExecutorAccountService:
    def __init__(self, service: AccountService, executor: ThreadPoolExecutor = None):
        # 📝 STEP 2: Initialize service and ThreadPoolExecutor
        self._service = service
        self._executor = executor or ThreadPoolFactory.new_fixed_pool(10)

    def open_account_async(self, *args, **kwargs) -> Future:
        # 📝 STEP 2: Submit open_account to executor and return Future
        return None

    def deposit_async(self, account_number: int, amount: float) -> Future:
        # 📝 STEP 2: Submit deposit to executor and return Future
        return None

    def withdraw_async(self, account_number: int, amount: float, pin: int) -> Future:
        # 📝 STEP 2: Submit withdraw to executor and return Future
        return None

    def transfer_async(self, from_account_number: int, to_account_number: int, amount: float, pin: int) -> Future:
        # 📝 STEP 2: Submit transfer to executor and return Future
        return None

    def shutdown(self) -> None:
        # 📝 STEP 2: Gracefully shutdown executor
        if self._executor:
            self._executor.shutdown(wait=True)

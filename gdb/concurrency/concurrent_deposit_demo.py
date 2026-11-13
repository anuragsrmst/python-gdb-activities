import threading
from gdb.service.account_service import AccountService

class ConcurrentDepositDemo:
    @staticmethod
    def run_demo(service: AccountService, account_number: int, threads: int = 10, ops_per_thread: int = 100, amount: float = 100.0) -> float:
        # 📝 STEP 1: Create start_event barrier, spawn worker threads, trigger together, and join
        return 0.0

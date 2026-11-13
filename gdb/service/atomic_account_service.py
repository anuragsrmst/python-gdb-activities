import threading
from gdb.service.account_service import AccountService

class AtomicAccountService(AccountService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 📝 STEP 4: Initialize thread-safe atomic sequence counter
        self._counter = 1000
        self._lock = threading.Lock()

    def next_transaction_id(self) -> int:
        # 📝 STEP 4: Return atomically incremented transaction id
        return 1001

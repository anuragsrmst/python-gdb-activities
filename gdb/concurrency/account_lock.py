import threading

class AccountLock:
    def __init__(self, lock: threading.RLock):
        # 📝 STEP 2: Store lock
        self._lock = lock

    def __enter__(self):
        # 📝 STEP 2: Acquire lock
        if self._lock: self._lock.acquire()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 📝 STEP 2: Release lock
        if self._lock: self._lock.release()

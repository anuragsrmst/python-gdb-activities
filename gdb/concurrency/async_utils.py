from concurrent.futures import ThreadPoolExecutor, Future
from typing import Callable, Any

class AsyncUtils:
    @staticmethod
    def supply_async(fn: Callable[[], Any], executor: ThreadPoolExecutor) -> Future:
        # 📝 STEP 1: Submit callable to executor
        return None

    @staticmethod
    def supply_with_default(fn: Callable[[], Any], default_val: Any, executor: ThreadPoolExecutor) -> Future:
        # 📝 STEP 1: Submit with fallback default on exception
        return None

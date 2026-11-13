from concurrent.futures import ThreadPoolExecutor

class ThreadPoolFactory:
    @staticmethod
    def new_fixed_pool(max_workers: int = 10) -> ThreadPoolExecutor:
        # 📝 STEP 1: Create and return ThreadPoolExecutor(max_workers=max_workers)
        return None

    @staticmethod
    def new_single_thread_executor() -> ThreadPoolExecutor:
        # 📝 STEP 1: Create single thread executor
        return None

    @staticmethod
    def shutdown_and_await(executor: ThreadPoolExecutor, timeout: float = 5.0) -> None:
        # 📝 STEP 1: Gracefully shutdown executor
        if executor:
            executor.shutdown(wait=True)

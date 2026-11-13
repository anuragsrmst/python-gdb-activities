import threading
from typing import List, Optional
from gdb.domain.iaccount import IAccount
from gdb.repository.account_repository import AccountRepository

class FileAccountRepository(AccountRepository):
    def __init__(self, file_path: str = "data/accounts.csv", backup_enabled: bool = True, max_backups: int = 5):
        self.file_path = file_path
        self.backup_enabled = backup_enabled
        self.max_backups = max_backups
        self._lock = threading.RLock()

    def save(self, account: IAccount) -> None:
        # 📝 STEP 4: Save account to CSV
        pass

    def find_by_id(self, account_number: int) -> Optional[IAccount]:
        # 📝 STEP 4: Find account by ID from CSV
        return None

    def find_all(self) -> List[IAccount]:
        # 📝 STEP 4: Retrieve all accounts from CSV
        return []

    def update(self, account: IAccount) -> None:
        # 📝 STEP 4: Update account in CSV
        pass

    def delete(self, account_number: int) -> None:
        # 📝 STEP 4: Delete account from CSV
        pass

    def exists(self, account_number: int) -> bool:
        # 📝 STEP 4: Check if account exists in CSV
        return False

    def next_account_number(self) -> int:
        # 📝 STEP 4: Generate next ID from CSV
        return 1001

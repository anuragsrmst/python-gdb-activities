from typing import Dict
from gdb.repository.account_repository import AccountRepository
from gdb.repository.transaction_repository import TransactionRepository

class DataMigrator:
    @staticmethod
    def migrate(src_acc: AccountRepository, dest_acc: AccountRepository,
                src_txn: TransactionRepository, dest_txn: TransactionRepository) -> Dict[str, int]:
        # 📝 STEP 5: Migrate all accounts and transactions from source to destination
        return {"accounts_migrated": 0, "transactions_migrated": 0}

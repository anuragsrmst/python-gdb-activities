from typing import Optional
from gdb.domain.iaccount import IAccount
from gdb.domain.transaction import Transaction

class CsvMapper:
    ACCOUNT_HEADER = "account_number,account_holder_name,age,balance,account_type,status,pin,opening_date,overdraft_used,interest_earned"
    TRANSACTION_HEADER = "transaction_id,timestamp,account_number,type,amount,balance_after,status,from_account,to_account,description"

    @staticmethod
    def to_csv_account(account: IAccount) -> str:
        # 📝 STEP 2: Serialize account to CSV
        return ""

    @staticmethod
    def from_csv_account(line: str) -> Optional[IAccount]:
        # 📝 STEP 2: Deserialize CSV to account
        return None

    @staticmethod
    def to_csv_transaction(txn: Transaction) -> str:
        # 📝 STEP 2: Serialize transaction to CSV
        return ""

    @staticmethod
    def from_csv_transaction(line: str) -> Optional[Transaction]:
        # 📝 STEP 2: Deserialize CSV to transaction
        return None

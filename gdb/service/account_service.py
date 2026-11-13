from typing import List, Optional
from gdb.domain.iaccount import IAccount
from gdb.domain.account_factory import AccountFactory
from gdb.domain.transaction import Transaction
from gdb.command.deposit_command import DepositCommand
from gdb.command.withdraw_command import WithdrawCommand
from gdb.command.transfer_command import TransferCommand
from gdb.command.transaction_command import TransactionCommand
from gdb.service.transfer_service import TransferService
from gdb.logging.transaction_logger import TransactionLogger
from gdb.repository.account_repository import AccountRepository
from gdb.repository.transaction_repository import TransactionRepository
from gdb.repository.repository_factory import RepositoryFactory
from gdb.exceptions.account_exception import AccountException
from gdb.exceptions.invalid_pin_exception import InvalidPinException

class AccountService:
    def __init__(self, account_repository: Optional[AccountRepository] = None,
                 transaction_repository: Optional[TransactionRepository] = None,
                 logger: Optional[TransactionLogger] = None):
        self._account_repository = account_repository or RepositoryFactory.get_account_repository()
        self._transaction_repository = transaction_repository or RepositoryFactory.get_transaction_repository()
        self._logger = logger
        self._transfer_service = TransferService()

    def open_account(self, account_type: str, name: str, age: int, initial_balance: float, tenure_years: int = 0) -> IAccount:
        account_number = self._account_repository.next_account_number()
        account = AccountFactory.create_account(account_type, account_number, name, age, initial_balance, tenure_years)
        self._account_repository.save(account)
        return account

    def get_account(self, account_number: int) -> Optional[IAccount]:
        return self._account_repository.find_by_id(account_number)

    def deposit(self, account_number: int, amount: float) -> Transaction:
        account = self.get_account(account_number)
        if account is None:
            raise AccountException(f"Account not found: {account_number}")
        cmd = DepositCommand(account, amount)
        cmd.execute()
        if self._account_repository is not None:
            self._account_repository.update(account)
        if self._transaction_repository is not None and cmd.get_transaction() is not None:
            self._transaction_repository.save(cmd.get_transaction())
        if self._logger is not None:
            self._logger.log(cmd)
        return cmd.get_transaction()

    def withdraw(self, account_number: int, amount: float, pin: int) -> Transaction:
        account = self.get_account(account_number)
        if account is None:
            raise AccountException(f"Account not found: {account_number}")
        cmd = WithdrawCommand(account, amount, pin)
        cmd.execute()
        if self._account_repository is not None:
            self._account_repository.update(account)
        if self._transaction_repository is not None and cmd.get_transaction() is not None:
            self._transaction_repository.save(cmd.get_transaction())
        if self._logger is not None:
            self._logger.log(cmd)
        return cmd.get_transaction()

    def transfer(self, from_account_number: int, to_account_number: int, amount: float, pin: int) -> Transaction:
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)
        if from_account is None:
            raise AccountException(f"Source account not found: {from_account_number}")
        if to_account is None:
            raise AccountException(f"Destination account not found: {to_account_number}")
        cmd = TransferCommand(from_account, to_account, amount, pin)
        cmd.execute()
        if self._account_repository is not None:
            self._account_repository.update(from_account)
            self._account_repository.update(to_account)
        if self._transaction_repository is not None and cmd.get_transaction() is not None:
            self._transaction_repository.save(cmd.get_transaction())
        if self._logger is not None:
            self._logger.log(cmd)
        return cmd.get_transaction()

    def close_account(self, account_number: int, pin: int) -> None:
        account = self.get_account(account_number)
        if account is None:
            raise AccountException(f"Account not found: {account_number}")
        if not account.verify_pin(pin):
            raise InvalidPinException("Incorrect PIN")
        account.close_account()
        if self._account_repository is not None:
            self._account_repository.update(account)

    def get_transaction_history(self) -> List[TransactionCommand]:
        return self._logger.read_all() if self._logger is not None else []

    def get_transaction_records(self, account_number: Optional[int] = None) -> List[Transaction]:
        if self._transaction_repository is None:
            return []
        if account_number is not None:
            return self._transaction_repository.find_by_account(account_number)
        return self._transaction_repository.find_all()

    def get_all_accounts(self) -> List[IAccount]:
        return self._account_repository.find_all() if self._account_repository is not None else []

from abc import ABC, abstractmethod
from typing import List
from gdb.domain.transaction import Transaction

class TransactionRepository(ABC):
    """
    Repository interface for transaction record storage, querying, and atomic balance transfers.
    """
    @abstractmethod
    def save(self, transaction: Transaction) -> None:
        pass

    @abstractmethod
    def find_by_account(self, account_number: int) -> List[Transaction]:
        pass

    @abstractmethod
    def find_all(self) -> List[Transaction]:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def transfer(self, from_account_number: int, to_account_number: int, amount: float) -> None:
        pass

from abc import ABC, abstractmethod
from typing import List, Optional
from gdb.domain.iaccount import IAccount

class AccountRepository(ABC):
    """
    Repository interface for account data access and persistence operations.
    Decouples domain and service layers from concrete storage implementations.
    """
    @abstractmethod
    def save(self, account: IAccount) -> None:
        pass

    @abstractmethod
    def find_by_id(self, account_number: int) -> Optional[IAccount]:
        pass

    @abstractmethod
    def find_all(self) -> List[IAccount]:
        pass

    @abstractmethod
    def update(self, account: IAccount) -> None:
        pass

    @abstractmethod
    def delete(self, account_number: int) -> None:
        pass

    @abstractmethod
    def exists(self, account_number: int) -> bool:
        pass

    @abstractmethod
    def next_account_number(self) -> int:
        pass

# gdb/domain/iaccount.py
from abc import ABC, abstractmethod

class IAccount(ABC):
    """Pure Interface defining the contract for all bank accounts."""
    # TODO (Step 1): Declare the full account contract as @abstractmethod members (each body is just `pass`):
    #   Methods:    deposit(amount) -> None, withdraw(amount) -> None, calculate_interest() -> float,
    #               display_account_info() -> None, validate_pin(entered_pin) -> bool, get_account_type() -> str
    #   Properties: account_number -> str, name -> str, age -> int, balance -> float, status -> str
    #               (stack @property on top of @abstractmethod for these)
    pass

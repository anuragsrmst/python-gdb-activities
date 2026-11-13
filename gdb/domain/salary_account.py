# gdb/domain/salary_account.py
from gdb.domain.abstract_account import AbstractAccount

class SalaryAccount(AbstractAccount):
    def __init__(self, account_number: str, name: str, age: int, balance: float, status: str = "Active", pin: str = "0000") -> None:
        super().__init__(account_number, name, age, balance, status, pin)

    def calculate_interest(self) -> float:
        # TODO: Salary accounts earn no interest -- return 0.0 to fulfil the IAccount contract.
        raise NotImplementedError("TODO: implement SalaryAccount.calculate_interest()")

    def get_account_type(self) -> str:
        # TODO: Return this product's type name, "Salary".
        raise NotImplementedError("TODO: implement SalaryAccount.get_account_type()")

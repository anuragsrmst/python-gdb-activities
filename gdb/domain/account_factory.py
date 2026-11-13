# gdb/domain/account_factory.py
# ACTIVITY 12: Replace this file with your completed Activity 11 version before writing the tests.
from gdb.domain.iaccount import IAccount
from gdb.domain.savings_account import SavingsAccount
from gdb.domain.current_account import CurrentAccount
from gdb.domain.salary_account import SalaryAccount
from gdb.domain.fixed_deposit_account import FixedDepositAccount
from gdb.exceptions import AccountException

class AccountFactory:
    """Factory creating IAccount instances based on type."""
    @staticmethod
    def create_account(account_type: str, account_number: str, name: str, age: int, balance: float, status: str = "Active", pin: str = "0000") -> IAccount:
        # TODO (Step 2): Create and return the IAccount implementation matching account_type.
        #   - None/empty account_type -> raise AccountException
        #   - Normalise with account_type.strip().upper(), then map:
        #       "SAVINGS"      -> SavingsAccount(...)       with interest_rate=4.0, minimum_balance=1000.0
        #       "CURRENT"      -> CurrentAccount(...)       with overdraft_limit=10000.0
        #       "SALARY"       -> SalaryAccount(...)
        #       "FIXEDDEPOSIT" -> FixedDepositAccount(...)  with tenure_months=12, interest_rate=6.5
        #   - Any other value -> raise AccountException naming the unknown type
        raise NotImplementedError("TODO: implement AccountFactory.create_account()")

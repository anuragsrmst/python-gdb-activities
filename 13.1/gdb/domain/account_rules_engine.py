# gdb/domain/account_rules_engine.py

class AccountRulesEngine:
    """Centralized Business Rules Engine for banking policies."""

    @staticmethod
    def get_minimum_balance(account_type: str) -> float:
        # TODO (Step 1): Return 1000.0 for "SAVINGS" and 0.0 for every other type.
        #   account_type may be None or mixed case -- normalise it with .strip().upper() first.
        raise NotImplementedError("TODO: implement AccountRulesEngine.get_minimum_balance()")

    @staticmethod
    def get_interest_rate(account_type: str) -> float:
        # TODO (Step 2): Return 4.0 for "SAVINGS", 6.5 for "FIXEDDEPOSIT", and 0.0 otherwise (including None/empty).
        raise NotImplementedError("TODO: implement AccountRulesEngine.get_interest_rate()")

    @staticmethod
    def get_overdraft_limit(account_type: str) -> float:
        # TODO (Step 2): Return 10000.0 for "CURRENT" and 0.0 otherwise (including None/empty).
        raise NotImplementedError("TODO: implement AccountRulesEngine.get_overdraft_limit()")

    @staticmethod
    def validate_withdrawal(account_type: str, current_balance: float, amount: float) -> bool:
        # TODO (Step 3): Combine the rules above. The lowest balance allowed after a withdrawal is
        #   (minimum balance - overdraft limit) for this account type. Return True if
        #   current_balance - amount stays at or above that floor, otherwise False.
        raise NotImplementedError("TODO: implement AccountRulesEngine.validate_withdrawal()")

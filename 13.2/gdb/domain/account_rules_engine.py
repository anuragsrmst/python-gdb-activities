# gdb/domain/account_rules_engine.py

class AccountRulesEngine:
    """Dynamic Dictionary-based Rules Engine."""
    # TODO (Step 1): Move every policy value out of your 13.1 if/else chains into this dictionary,
    #   keyed by upper-case account type ("SAVINGS", "CURRENT", "SALARY", "FIXEDDEPOSIT"), e.g.
    #   "SAVINGS": {"min_balance": ..., "interest_rate": ..., "overdraft_limit": ...}
    _RULES: dict = {}

    @classmethod
    def get_minimum_balance(cls, account_type: str) -> float:
        # TODO (Step 2): Look "min_balance" up in cls._RULES (O(1), no if/else chain).
        #   Return 0.0 for None/empty or unknown types (hint: dict.get() with a default).
        raise NotImplementedError("TODO: implement AccountRulesEngine.get_minimum_balance()")

    @classmethod
    def get_interest_rate(cls, account_type: str) -> float:
        # TODO (Step 2): Look "interest_rate" up in cls._RULES; 0.0 for None/empty or unknown types.
        raise NotImplementedError("TODO: implement AccountRulesEngine.get_interest_rate()")

    @classmethod
    def get_overdraft_limit(cls, account_type: str) -> float:
        # TODO (Step 2): Look "overdraft_limit" up in cls._RULES; 0.0 for None/empty or unknown types.
        raise NotImplementedError("TODO: implement AccountRulesEngine.get_overdraft_limit()")

    @classmethod
    def validate_withdrawal(cls, account_type: str, current_balance: float, amount: float) -> bool:
        min_bal = cls.get_minimum_balance(account_type)
        overdraft = cls.get_overdraft_limit(account_type)
        return (current_balance - amount) >= (min_bal - overdraft)

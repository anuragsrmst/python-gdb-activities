# gdb/domain/account_rules_engine.py
from gdb.domain.account_rules_properties_loader import AccountRulesPropertiesLoader

class AccountRulesEngine:
    """Properties-Driven Rules Engine."""
    # TODO: Replace the hard-coded rules from Activity 13. Each getter loads the account type's
    #   properties with AccountRulesPropertiesLoader.load_rules(account_type) and returns the value
    #   for its key converted to float (0.0 when the key is missing).

    @staticmethod
    def get_minimum_balance(account_type: str) -> float:
        # TODO: Return the "minBalance" property as a float.
        raise NotImplementedError("TODO: implement AccountRulesEngine.get_minimum_balance()")

    @staticmethod
    def get_interest_rate(account_type: str) -> float:
        # TODO: Return the "interestRate" property as a float.
        raise NotImplementedError("TODO: implement AccountRulesEngine.get_interest_rate()")

    @staticmethod
    def get_overdraft_limit(account_type: str) -> float:
        # TODO: Return the "overdraftLimit" property as a float.
        raise NotImplementedError("TODO: implement AccountRulesEngine.get_overdraft_limit()")

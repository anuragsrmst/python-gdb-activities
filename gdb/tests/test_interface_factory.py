# gdb/tests/test_interface_factory.py
from gdb.domain.account_factory import AccountFactory

def main():
    print("=== Activity 12: Factory-Driven System Suite ===")

    # TODO (Step 1): Create one account of each type ONLY through AccountFactory.create_account():
    #   "SAVINGS", "CURRENT", "SALARY" and "FIXEDDEPOSIT"
    #   (arguments: account_type, account_number, name, age, balance, status, pin).

    # TODO (Step 2): Using only IAccount members (no concrete class names), assert that each account
    #   balance and get_account_type() match what you created, then exercise deposit()/withdraw().

if __name__ == "__main__":
    main()

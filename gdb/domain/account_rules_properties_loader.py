# gdb/domain/account_rules_properties_loader.py
import os

class AccountRulesPropertiesLoader:
    """Utility loading external .properties files."""

    @staticmethod
    def load_rules(account_type: str) -> dict:
        # TODO (Step 2): Load gdb/resources/config/rules/<account_type in lower case>.properties into a dict.
        #   1. Build the path relative to this module so it works from any working directory, e.g.
        #      os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "resources", "config", "rules", ...)
        #   2. If the file does not exist, return an empty dict.
        #   3. Read it line by line (encoding="utf-8"); skip blank lines and lines starting with "#".
        #   4. Split each remaining "key=value" line on the FIRST "=" and store the stripped key and value strings.
        raise NotImplementedError("TODO: implement AccountRulesPropertiesLoader.load_rules()")

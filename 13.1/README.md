# Activity 13.1: Rules Engine (If-Else)

## Objective
Extract policy thresholds and business logic out of domain models into a centralized `AccountRulesEngine` using clean conditional evaluations.

---

## Target Files to Complete
- `gdb/domain/account_rules_engine.py`

---

## Plain English Step-by-Step Instructions

### Step 1: Implement Minimum Balance Rules
1. In `get_minimum_balance(account_type)`:
   - Return `1000.0` for `"SAVINGS"` and `0.0` for other account types.

### Step 2: Implement Interest Rate & Overdraft Rules
1. In `get_interest_rate(account_type)`:
   - Return `4.0` for `"SAVINGS"`, `6.5` for `"FIXEDDEPOSIT"`, `0.0` for others.
2. In `get_overdraft_limit(account_type)`:
   - Return `10000.0` for `"CURRENT"`, `0.0` for others.

### Step 3: Implement Withdrawal Rule Validation
1. Combine minimum balance and overdraft limits in `validate_withdrawal()`.

---

## How to Run (Multi-OS Guide)
Run these commands from inside this activity folder (the folder that contains `gdb/`).

### Windows (PowerShell)
```powershell
python -m gdb.tests.test_account_rules_engine
```

### Windows (Command Prompt - CMD)
```cmd
python -m gdb.tests.test_account_rules_engine
```

### Linux & macOS (Terminal / Bash / Zsh)
```bash
python3 -m gdb.tests.test_account_rules_engine
```

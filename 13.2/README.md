# Activity 13.2: Rules Engine Integration

## Objective
Refactor the Rules Engine to use fast, dynamic dictionary lookups and verify multi-product policy validation.

---

## Target Files to Complete
- `gdb/domain/account_rules_engine.py`

---

## Plain English Step-by-Step Instructions

### Step 1: Refactor Rules into Dictionary
1. Store policy parameters in a dictionary keyed by account type.
2. Provide O(1) lookup methods for minimum balance, interest rates, and overdraft limits.

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

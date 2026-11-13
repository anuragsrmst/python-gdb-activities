# Activity 12: Testing Interface and Factory

## Objective
Write an end-to-end integration test driver verifying that client applications can interact with all account types exclusively through `IAccount` and `AccountFactory`.

---

## Target Files to Complete
- `gdb/tests/test_interface_factory.py`

---

## Plain English Step-by-Step Instructions

### Step 1: Interface-Only Client Testing
1. Instantiate all four account types using `AccountFactory.create_account()`.
2. Exercise methods and assert properties purely through interface methods.

---

## How to Run (Multi-OS Guide)
Run these commands from inside this activity folder (the folder that contains `gdb/`).

### Windows (PowerShell)
```powershell
python -m gdb.tests.test_interface_factory
```

### Windows (Command Prompt - CMD)
```cmd
python -m gdb.tests.test_interface_factory
```

### Linux & macOS (Terminal / Bash / Zsh)
```bash
python3 -m gdb.tests.test_interface_factory
```

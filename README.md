# Activity 11: IAccount Interface and Factory Pattern

## Objective
Decouple client code from concrete constructors using the `IAccount` interface contract and the `AccountFactory` design pattern.

---

## Target Files to Complete
- `gdb/domain/iaccount.py`
- `gdb/domain/abstract_account.py`
- `gdb/domain/salary_account.py`
- `gdb/domain/account_factory.py`

---

## Plain English Step-by-Step Instructions

### Step 1: Declare `IAccount(ABC)` Interface
1. Define abstract methods and properties for all bank account operations.

### Step 2: Implement `AccountFactory`
1. In `create_account(account_type, ...) -> IAccount`, instantiate and return the corresponding account subclass.

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

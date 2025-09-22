# 🧾 User Registration Mini Project

This is a simple Python project to demonstrate **unit testing** and **integration testing** using `pytest`.

---

## 📁 Project Structure

```
user_project/
├── auth.py # Username validation logic
├── db.py # Fake in-memory "database"
├── register.py # Registration workflow using auth + db
├── test_unit.py # Unit tests for individual modules
└── test_integration.py # Integration tests for the full flow
```

---

## 🧠 Description

### Modules:

- `auth.py`  
  → Validates username (alphanumeric, ≥ 3 characters)

- `db.py`  
  → Simulates a database using a Python list

- `register.py`  
  → Combines `auth` and `db` to register a user

---

## 🔬 Testing Breakdown

### ✅ Unit Tests (`test_unit.py`)
Tests:
- `auth.is_valid_username()`
- `db.save_user()` and `db.user_exists()`

### 🔗 Integration Tests (`test_integration.py`)
Tests:
- Full registration flow:
  - Registering a valid user
  - Duplicate user
  - Invalid username

---

## ▶️ How to Run the Tests

### 🧪 Step 1: Install `pytest` (if not installed)

```
pip install pytest
```
### 🧪 Step 2: Run All Tests
- From inside the user_project/ folder:
  ```
  pytest
  ```
### ✅ Expected Output
```
test_unit.py ..............        [unit tests passed]
test_integration.py .......        [integration tests passed]
```
## 💡 Concepts Covered

✅ **Unit Testing**  
Test individual functions or components in isolation to ensure they work as expected.

🔁 **Integration Testing**  
Verify that different modules (auth, db, register) interact correctly when combined.

🧪 **Writing Clean and Maintainable Tests with `pytest`**  
Use `assert` statements and organize test files properly for clarity and reusability.

📦 **Fake Database Simulation**  
Use an in-memory Python list (`fake_db`) to simulate database behavior without needing a real database.

🧱 **Simple Modular Design in Python**  
Code is separated into small, single-responsibility modules (`auth.py`, `db.py`, `register.py`) to promote clarity, maintainability, and easier testing.

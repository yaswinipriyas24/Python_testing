from register import register_user
from db import fake_db

def test_register_user_integration():
    fake_db.clear()

    # Valid new user
    result1 = register_user("newuser")
    assert result1 == "User registered successfully"

    # Same user again
    result2 = register_user("newuser")
    assert result2 == "User already exists"

    # Invalid username
    result3 = register_user("!!")
    assert result3 == "Invalid username"

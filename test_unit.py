import auth
import db

def test_is_valid_username():
    assert auth.is_valid_username("user123")
    assert not auth.is_valid_username("us")  # too short
    assert not auth.is_valid_username("user!@")  # special chars

def test_save_and_check_user():
    db.fake_db.clear()  # reset db
    assert db.save_user("testuser") == True
    assert db.user_exists("testuser") == True
    assert db.user_exists("unknown") == False

fake_db = []

def save_user(username):
    fake_db.append(username)
    return True

def user_exists(username):
    return username in fake_db

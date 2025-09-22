def is_valid_username(username):
    return username.isalnum() and len(username) >= 3

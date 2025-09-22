from auth import is_valid_username
from db import user_exists, save_user

def register_user(username):
    if not is_valid_username(username):
        return "Invalid username"
    if user_exists(username):
        return "User already exists"
    save_user(username)
    return "User registered successfully"

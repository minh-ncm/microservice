from backend.services.auth.handlers import *


def test_password_handler():
    handler = PasswordHandler()
    hashed_password = handler.hash_raw_password('qwer')
    print(hashed_password)
    print(handler.verify_password('qwer', hashed_password))
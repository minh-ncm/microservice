from passlib.context import CryptContext


class PasswordHandler:
    def __init__(self) -> None:
        self.pwd_context = CryptContext(schemes=['sha256_crypt'], deprecated='auto')


    def hash_raw_password(self, raw_password:str):
        return self.pwd_context.hash(raw_password)


    def verify_password(self, raw_password:str, hashed_password:str):
        return self.pwd_context.verify(raw_password, hashed_password)
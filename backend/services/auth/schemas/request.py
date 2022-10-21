from pydantic import BaseModel
from typing import Union, Optional
from bson.objectid import ObjectId

from ..handlers import PasswordHandler


class LoginRequestSchema(BaseModel):
    username: str
    password: str


class RegisterRequestSchema(BaseModel):
    username: str
    password: str


    def encode_password(self):
        password_handler = PasswordHandler()
        encoded = password_handler.hash_raw_password(self.password)
        self.password = encoded
        return self


class QueryUserRequestSchema(BaseModel):
    username: Optional[str]
    user_id: Optional[str]

from datetime import datetime, timedelta
from jose import jwt
from typing import Dict, Union

from backend.services.auth.env import env


class TokenHandler:
    def __init__(self) -> None:
        self.secret = env.SECRET_KEY_AUTH
        self.algorithm = 'HS256'


    def create_access_token(self, data:Dict, expired_delta: Union[timedelta, None]=None):
        coppied_data = data.copy()
        
        if expired_delta:
            expire = datetime.utcnow() + expired_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        coppied_data.update({'exp': expire})

        encoded_jwt = jwt.encode(coppied_data, self.secret, self.algorithm)
        return encoded_jwt
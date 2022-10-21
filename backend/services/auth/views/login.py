from ..handlers import UserHandler, PasswordHandler
from ..models import User
from ..schemas import RegisterRequestSchema, LoginRequestSchema, QueryUserRequestSchema
from backend.commons.exceptions import WebException
from backend.commons import constants


async def login_view(user_info:LoginRequestSchema):
    user_handler = UserHandler()
    password_handler = PasswordHandler()

    user = await user_handler.query_user(QueryUserRequestSchema(username=user_info.username))
    user: User
    if user:
        if password_handler.verify_password(user_info.password, user.password):
            return {}
    raise WebException(**constants.STATUS_UNAUTHORIZED_LOGIN.dict())


async def register_view(user_info:RegisterRequestSchema):
    user_handler = UserHandler()
    new_user = await user_handler.create_user(user_info)
    return new_user
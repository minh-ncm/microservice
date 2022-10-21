from ..models import User
from ..schemas import QueryUserRequestSchema, RegisterRequestSchema


class UserHandler:
    async def query_user(self, request_data:QueryUserRequestSchema):
        query = {}
        if request_data.user_id:
            query.update({'user_id': request_data.user_id})
        if request_data.username:
            query.update({'username': request_data.username})

        user = await User.find_one(query)
        return user


    async def create_user(self, request_data:RegisterRequestSchema):
        new_user = User(**request_data.dict())
        await new_user.commit()
        return new_user
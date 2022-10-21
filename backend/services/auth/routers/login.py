from fastapi import APIRouter

from ..views import login_view, token_view, register_view
from ..schemas import RegisterRequestSchema, LoginRequestSchema
from backend.commons.schemas import ResponseSchema


router = APIRouter()


@router.post('/login', response_model=ResponseSchema, tags=['Authentication'])
async def login(user_info:LoginRequestSchema):
    data = await login_view(user_info)
    return data


@router.post('/token', response_model=ResponseSchema, tags=['Authentication'])
async def token():
    data = await token_view()
    return data


@router.post('/register', response_model=ResponseSchema, tags=['Authentication'])
async def register(user_info:RegisterRequestSchema):
    user_info.encode_password()
    data = await register_view(user_info)
    return {}
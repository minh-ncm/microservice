from fastapi import APIRouter


router = APIRouter(prefix='/author')


@router.post('/role/create')
async def create_role():
    pass
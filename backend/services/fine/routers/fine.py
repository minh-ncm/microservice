from fastapi import APIRouter

from ..schemas import QueryFineRequestSchema, FineCreateRequestSchema, FineUpdateRequestSchema
from backend.commons.schemas import ResponseSchema
from ..views import get_fine_view, insert_fine_view, update_fine_view


router = APIRouter(tags=['CRUD Fine'])


@router.post('/get', response_model=ResponseSchema)
async def get_fine_data(request_data:QueryFineRequestSchema):
    data = await get_fine_view(request_data)
    return {'data': data}


@router.post('/insert', response_model=ResponseSchema)
async def insert_fine(request_data:FineCreateRequestSchema):
    data = await insert_fine_view(request_data)
    return {'data': [data]}


@router.post('/update', response_model=ResponseSchema)
async def update_fine(request_data:FineUpdateRequestSchema):
    data = await update_fine_view(request_data)
    return {'data': [data]}
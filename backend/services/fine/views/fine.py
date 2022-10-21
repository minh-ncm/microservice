from ..schemas import QueryFineRequestSchema, FineCreateRequestSchema, FineUpdateRequestSchema
from ..handlers import FineHandler


async def get_fine_view(request_data:QueryFineRequestSchema):
    fine_handler = FineHandler()
    data = await fine_handler.query_data(request_data)
    return data


async def insert_fine_view(request_data:FineCreateRequestSchema):
    fine_handler = FineHandler()
    data = await fine_handler.insert_data(request_data)
    return data


async def update_fine_view(request_data:FineUpdateRequestSchema):
    fine_handler = FineHandler()
    data = await fine_handler.update_data(request_data)
    return data
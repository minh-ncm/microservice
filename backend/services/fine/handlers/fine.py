from datetime import datetime

from ..models import Fine
from ..schemas import QueryFineRequestSchema, FineCreateRequestSchema, FineUpdateRequestSchema
from backend.commons.utils import convert_str_objectid


class FineHandler:
    async def query_data(self, request_data:QueryFineRequestSchema):
        query = {
            'created_at': {'$gte': request_data.from_datetime},
            'updated_at': {'$lte': request_data.to_datetime},
        }
        if request_data.fine_status:
            query.update({'status': request_data.fine_status})

        fine_list = await Fine.find(query).to_list(None)
        fine_list = [data.dump() for data in fine_list]
        return fine_list


    async def insert_data(self, request_data:FineCreateRequestSchema):
        new_fine = Fine(**request_data.dict(), created_at=datetime.utcnow(), updated_at=datetime.utcnow())
        await new_fine.commit()
        return new_fine


    async def update_data(self, request_data:FineUpdateRequestSchema):
        fine = await Fine.find_one({'_id': convert_str_objectid(request_data.fine_id)})
        fine: Fine
        for key, value in request_data.dict().items():
            if value:
                setattr(fine, key, value)
        fine.updated_at(datetime.utcnow())
        await fine.commit()
        return fine
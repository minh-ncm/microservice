from pydantic import BaseModel, validator
from typing import Optional, Union
from datetime import datetime


class QueryFineRequestSchema(BaseModel):
    user_id: Optional[str]
    fine_status: Optional[int]
    from_datetime: datetime = None
    to_datetime: datetime = None

    @validator('from_datetime', 'to_datetime')
    def valdate_datetime(cls, value, values, config, field):
        print(value, field)
        if value is None:
            if field == 'from_datetime':
                return datetime.min
            elif field == 'to_datetime':
                return datetime.max

        return value

    
class FineCreateRequestSchema(BaseModel):
    username: str
    amount: int
    desc: str


class FineUpdateRequestSchema(BaseModel):
    fine_id: str
    amount: Optional[int]
    desc: Optional[str]
    status: Optional[int]
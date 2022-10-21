from pydantic import BaseModel
from typing import List

from .. import constants


class ResponseSchema(BaseModel):
    is_error: bool = False
    code: int = constants.STATUS_OK.code
    msg: str = constants.STATUS_OK.msg
    data: List = []
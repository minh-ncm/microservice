from typing import Union
from bson.objectid import ObjectId

from .. import constants
from ..exceptions import WebException


def convert_str_objectid(value:Union[str, ObjectId]):
    if isinstance(value, ObjectId):
        return str(value)
    elif isinstance(value, str):
        return ObjectId(value)
    else:
        raise WebException(**constants.STATUS_NOT_IMPLEMENTED.dict())

from pydantic import BaseModel


class ResponseStatusSchema(BaseModel):
    code: int
    msg: str


STATUS_OK = ResponseStatusSchema(code=200000, msg='Ok')
STATUS_BAD_REQUEST = ResponseStatusSchema(code=400000, msg='Bad Request')
STATUS_BAD_REQUEST_DUP_USERNAME = ResponseStatusSchema(code=400001, msg='Username already existed')
STATUS_UNAUTHORIZED = ResponseStatusSchema(code=401000, msg='Unauthorized')
STATUS_UNAUTHORIZED_LOGIN = ResponseStatusSchema(code=401001, msg='Wrong username or password')
STATUS_FORBIDDEN = ResponseStatusSchema(code=403000, msg='Forbidden')
STATUS_NOT_FOUND = ResponseStatusSchema(code=404000, msg='Not Found')
STATUS_SERVER_ERROR = ResponseStatusSchema(code=500000, msg='Internal Server Error')
STATUS_NOT_IMPLEMENTED = ResponseStatusSchema(code=50100, msg='Not Implemented')
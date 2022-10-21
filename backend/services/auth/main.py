from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from backend.commons import constants
from .routers import ROUTER_LIST
from backend.commons.exceptions import WebException


web_app = FastAPI()


for router in ROUTER_LIST:
    web_app.include_router(router, prefix='/api/auth')


@web_app.exception_handler(WebException)
async def web_exception_handler(request:Request, exception:WebException):
    return JSONResponse(content=exception.dict())


@web_app.exception_handler(RequestValidationError)
async def request_validate_handler(request:Request, exception:RequestValidationError):
    return JSONResponse(content=constants.STATUS_BAD_REQUEST.dict())
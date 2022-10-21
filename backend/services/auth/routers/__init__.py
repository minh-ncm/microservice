from .login import router as login_router
from .authorization import router as authorize_router


ROUTER_LIST = [
    login_router,
    authorize_router,
]
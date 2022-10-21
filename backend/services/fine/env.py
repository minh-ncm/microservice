from pydantic import BaseSettings


class Env(BaseSettings):
    APP_HOST: str
    APP_PORT: int

    SECRET_KEY_FINE: str

    ENV_MONGO_HOST_FINE: str
    ENV_MONGO_PORT_FINE: int
    MONGO_USERNAME_FINE: str
    MONGO_PASSWORD_FINE: str
    MONGO_DB_NAME_FINE: str
    MONGO_URI_FINE: str


env = Env(_env_file='.env')
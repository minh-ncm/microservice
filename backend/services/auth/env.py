from pydantic import BaseSettings


class Env(BaseSettings):
    APP_HOST: str
    APP_PORT: int

    SECRET_KEY_AUTH: str

    ENV_MONGO_HOST_AUTH: str
    ENV_MONGO_PORT_AUTH: int
    MONGO_USERNAME_AUTH: str
    MONGO_PASSWORD_AUTH: str
    MONGO_DB_NAME_AUTH: str
    MONGO_URI_AUTH: str


env = Env(_env_file='.env')
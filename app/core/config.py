from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "A Happy Space"
    VERSION: str = "0.0.1"
    AUTH_TOKEN: str = "token"
from pydantic import BaseSettings

from os import getenv


class Settings(BaseSettings):
    commit: str = getenv('COMMIT')
    description: str = "URL shortener"
    name: str = "Shortly"
    base_path: str = "/shortly/api"

    class Config:
        case_sensitive = True


settings = Settings()

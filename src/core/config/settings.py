import os

from pathlib import Path
from pydantic_settings import BaseSettings


BASE_PATH = Path(__file__).resolve().parent.parent.parent.parent
LOG_PATH = os.path.join(BASE_PATH, 'logs')


class Settings(BaseSettings):

    # FastAPI
    TITLE: str = 'Forms'
    DESCRIPTION: str = 'check forms'
    VERSION: str = '0.1'
    DOCS_URL: str | None = '/docs'
    REDOCS_URL: str | None = '/redocs'
    DEBUG: bool

    # Log
    LOG_FILENAME: str = 'tg_bot.log'
    DEBUG: str

    # test
    TEST_URL: str = 'http://127.0.0.1:8000/get_form'


settings = Settings()

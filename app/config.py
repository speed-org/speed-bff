from os import getenv
from dotenv import load_dotenv

load_dotenv()


class Config:
    ALLOWED_ORIGINS = getenv('ALLOWED_ORIGINS', '*')
    API_VERSION = getenv('API_VERSION', 'v1')
    SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI', '')
    SECRET_KEY = getenv('SECRET_KEY', '')
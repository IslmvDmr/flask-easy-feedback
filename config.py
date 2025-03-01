import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGIN_MESSAGE = os.getenv('LOGIN_MESSAGE')
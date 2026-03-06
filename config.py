from os import environ
from dotenv import load_dotenv

load_dotenv()
print(environ.get("DATABASE_URI"))


class Config:
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False      
          
    SQLALCHEMY_ECHO = True
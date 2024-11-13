import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///vawt_data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

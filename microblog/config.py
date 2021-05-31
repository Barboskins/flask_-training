import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:amibamcx3700@localhost:5432/microblog_fl'
    SQLALCHEMY_TRACK_MODIFICATIONS = False



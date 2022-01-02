import os


class BaseConfig:
    API_PREFIX = '/api'
    TESTING = False
    DEBUG = False
    __db_user = os.environ.get('DATABASE_USER', 'postgres')
    __db_pw = os.environ.get('DATABASE_PASSWORD', 'postgres')
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@db-postgres:5432/flask-deploy'.format(__db_user, __db_pw)


class DevConfig(BaseConfig):
    FLASK_ENV = 'development'
    DEBUG = True


class ProductionConfig(BaseConfig):
    FLASK_ENV = 'production'


class TestConfig(BaseConfig):
    FLASK_ENV = 'development'
    TESTING = True
    DEBUG = True

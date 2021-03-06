import os
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    TESTING = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    TESTING = True
    FLASK_ENV = "development"
    DEBUG = True



class TestingConfig(Config):
    TESTING = True


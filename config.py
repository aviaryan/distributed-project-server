import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
# SQLITE_PATH = 'sqlite:///' + DIR_PATH + '/database.sqlite3'


class Config(object):
    DEBUG = True
    CSRF_ENABLED = True
    SECRET_KEY = 'abcdefgh'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class LocalConfig(Config):
    pass


class ProductionConfig(Config):
    DEBUG = False


class HerokuConfig(ProductionConfig):
    DEBUG = True


class SQLiteConfig(Config):
    pass

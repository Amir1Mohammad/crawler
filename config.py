# Python imports
import os

# Flask imports

# Project imports


__Author__ = "Amir Mohammad"

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '_5#y2L"F4Q8zthis]/'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = "postgresql://postgres:asDCE23dfcaWsdE555mleEWf@localhost/pgdb"
    # postgresql://username:password@hostname/database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    JSON_AS_ASCII = False

    ANNOUNCEMENTS_PER_PAGE = 20
    LOG_PER_PAGE = 40

    CACHE_TYPE = "simple"  # Flask-Caching related configs
    CACHE_DEFAULT_TIMEOUT = 360
    CELERY_RESULT_BACKEND = SQLALCHEMY_DATABASE_URI


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

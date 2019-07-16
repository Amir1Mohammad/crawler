# Python imports
from celery import Celery

# Flask imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_caching import Cache

# Project imports
from config import Config

# from controller import user, scraper, api, errors

__Author__ = "Amir Mohammad"

app = Flask(__name__, template_folder='../template', static_folder='../static')
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)

cache = Cache(app)
cache.init_app(app)

app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

from controller import user, scraper, api, errors, auth

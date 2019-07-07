# Python imports

# Flask imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Project imports
from config import Config

__Author__ = "Amir Mohammad"

app = Flask(__name__, template_folder='../template', static_folder='../static')
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)


from controller import user, basket

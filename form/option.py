# Python imports

# Flask imports
from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField


# Project imports


__Author__ = "Amir Mohammad"


class OptionBazaar(FlaskForm):
    power = BooleanField()
    submit = SubmitField('start')
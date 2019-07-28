# Python imports

# Flask imports
from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, IntegerField
from wtforms.validators import NumberRange, DataRequired

# Project imports


__Author__ = "Amir Mohammad"


class OptionBazaar(FlaskForm):
    power = BooleanField('Power')
    body = IntegerField('Set Category', validators=[DataRequired(), NumberRange(1, 5)])
    sleep_from = IntegerField('sleep from', validators=[DataRequired(), NumberRange(0, 60)])
    sleep_to = IntegerField('sleep to', validators=[DataRequired(), NumberRange(0, 60)])
    submit = SubmitField('start')

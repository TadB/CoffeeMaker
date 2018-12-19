from flask_wtf import FlaskForm
from wtforms import SubmitField


class CoffeeTypesForm(FlaskForm):
    submit = SubmitField('Espresso')

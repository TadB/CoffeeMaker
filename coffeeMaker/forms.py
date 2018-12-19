from flask_wtf import FlaskForm
from wtforms import SubmitField


class CoffeeTypesForm(FlaskForm):
    espresso = SubmitField('Espresso')
    latte = SubmitField('Caffè latte')
    americano = SubmitField('Caffè americano')
    cappucino = SubmitField('Cappuccino')

from flask_wtf import FlaskForm
from wtforms import SubmitField


class CoffeeTypesForm(FlaskForm):
    espresso = SubmitField('Espresso')
    latte = SubmitField('Caffè latte')
    americano = SubmitField('Caffè americano')
    cappucino = SubmitField('Cappuccino')


class ServiceForm(FlaskForm):
    water = SubmitField('Water Tank')
    milk = SubmitField('Milk Tank')
    grounds = SubmitField('Grounds Tank')
    beans = SubmitField('Beans Tank')

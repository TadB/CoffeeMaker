from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import Optional


class CoffeeTypesForm(FlaskForm):
    espresso = SubmitField('Espresso')
    latte = SubmitField('Caffè latte')
    americano = SubmitField('Caffè americano')
    cappucino = SubmitField('Cappuccino')


class ServiceForm(FlaskForm):
    water_int = IntegerField(validators=[Optional()], label="Water Tank")
    milk_int = IntegerField(validators=[Optional()], label="Milk Tank")
    grounds_int = IntegerField(validators=[Optional()], label="Grounds Tank")
    beans_int = IntegerField(validators=[Optional()], label="Beans Tank")
    submit = SubmitField(label='Refill')

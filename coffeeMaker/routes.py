from coffeeMaker import app
from flask import render_template, flash, redirect
from coffeeMaker.forms import CoffeeTypesForm

@app.route("/", methods=['GET', 'POST'])
def home():
    form = CoffeeTypesForm()
    return render_template('choose_coffee.html', title='Select delicious coffee', form=form)
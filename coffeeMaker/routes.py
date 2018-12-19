from flask import render_template, url_for, redirect, flash
from coffeeMaker import app
from coffeeMaker.forms import CoffeeTypesForm, ServiceForm
from coffeeMaker.utils import make_coffee, full_refill
from coffeeMaker.models import Tank

tanks = Tank.query.all()


@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html', tanks=tanks)


@app.route("/choose", methods=['GET', 'POST'])
def main_panel():
    form = CoffeeTypesForm()
    if form.validate_on_submit():
        if form.espresso.data:
            coffee_type = form.espresso.label.text
        elif form.latte.data:
            coffee_type = form.latte.label.text
        elif form.americano.data:
            coffee_type = form.americano.label.text
        elif form.cappucino.data:
            coffee_type = form.cappucino.label.text
        check = make_coffee(coffee_type)
        if check is True:
            flash('Enjoy Your Coffee!', 'success')
        else:
            # flash('Not enought ingredients', 'warning')
            flash(check, 'warning')
        return redirect(url_for('home'))
    return render_template(
        'choose_coffee.html', title='Select delicious coffee',
        form=form, tanks=tanks)


@app.route("/service", methods=['GET', 'POST'])
def service():
    form = ServiceForm()
    if form.validate_on_submit():
        if form.water.data:
            tank_type = form.water.label.text
        elif form.milk.data:
            tank_type = form.milk.label.text
        elif form.grounds.data:
            tank_type = form.grounds.label.text
        elif form.beans.data:
            tank_type = form.beans.label.text
        if full_refill(tank_type):
            flash(f'{tank_type} refilled!', 'success')
        else:
            flash(f'{tank_type} is full - no need to refill', 'info')
        return redirect(url_for('service'))
    return render_template(
        'service.html', title='Service menu', form=form, tanks=tanks)

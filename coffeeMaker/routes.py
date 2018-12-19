from flask import render_template, url_for, redirect
from coffeeMaker import app
from coffeeMaker.forms import CoffeeTypesForm, ServiceForm
from coffeeMaker.utils import make_coffee, full_refill


@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html')


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
        make_coffee(coffee_type)
        return redirect(url_for('home'))
    return render_template(
        'choose_coffee.html', title='Select delicious coffee', form=form)


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
        full_refill(tank_type)
        return redirect(url_for('service'))
    return render_template('service.html', title='Service menu', form=form)

from flask import render_template, url_for, redirect, flash
from coffeeMaker import app
from coffeeMaker.forms import CoffeeTypesForm, ServiceForm
from coffeeMaker.utils import make_coffee, refill
from coffeeMaker.models import Tank


@app.route("/home")
@app.route("/")
def home():
    tanks = Tank.query.all()
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
            flash(check, 'warning')
        return redirect(url_for('home'))
    tanks = Tank.query.all()
    return render_template(
        'choose_coffee.html', title='Select delicious coffee',
        form=form, tanks=tanks)


@app.route("/service", methods=['GET', 'POST'])
def service():
    form = ServiceForm()
    if form.validate_on_submit():
        for field in form:
            if field.data and field.name is not "submit":
                refill_amount = field.data
                if isinstance(field.data, int):
                    tank_type = field.label.text
                    result = refill(tank_type, refill_amount)
                    flash(f'{result}', 'info')
        return redirect(url_for('service'))
    tanks = Tank.query.all()
    return render_template(
        'service.html', title='Service menu', form=form, tanks=tanks)

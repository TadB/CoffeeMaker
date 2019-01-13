from flask import render_template, url_for, redirect, flash
# from coffeeMaker import app
from coffeeMaker.main.forms import CoffeeTypesForm, ServiceForm
from coffeeMaker.utils import make_coffee, refill
from coffeeMaker.models import Tank
from coffeeMaker.main import bp


@bp.route("/home")
@bp.route("/")
def home():
    tanks = Tank.query.all()
    return render_template('home.html', tanks=tanks)


@bp.route("/choose", methods=['GET', 'POST'])
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
        return redirect(url_for('main.home'))
    tanks = Tank.query.all()
    return render_template(
        'choose_coffee.html', title='Select delicious coffee',
        form=form, tanks=tanks)


@bp.route("/service", methods=['GET', 'POST'])
def service():
    form = ServiceForm()
    if form.validate_on_submit():
        for field in form:
            if field.name is not "submit":
                try:
                    refill_amount = int(field.data)
                    tank_type = field.label.text
                    result = refill(tank_type, refill_amount)
                    flash(f'{result}', 'info')
                except ValueError:
                    pass
                # because 0 is not accepted in wtforms as number but False/None
                except TypeError:
                    if type(field.data) is None:
                        result = refill(field.label.text, 0)
                        flash(f'{result}', 'info')
        return redirect(url_for('main.service'))
    tanks = Tank.query.all()
    return render_template(
        'service.html', title='Service menu', form=form, tanks=tanks)

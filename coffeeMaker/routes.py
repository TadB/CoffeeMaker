from flask import render_template, url_for, redirect
from coffeeMaker import app
from coffeeMaker.forms import CoffeeTypesForm
from coffeeMaker.utils import make_coffee


@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html')


@app.route("/choose", methods=['GET', 'POST'])
def main_panel():
    form = CoffeeTypesForm()
    if form.validate_on_submit():
        input = str(form.submit.label.text)
        make_coffee(input)
        return redirect(url_for('home'))
    return render_template(
        'choose_coffee.html', title='Select delicious coffee', form=form)

from coffeeMaker.models import Coffee, Tank
from coffeeMaker import db
import json

with open('coffee_types.json') as f:
    coffee_json = json.load(f)

for coffee in coffee_json:
    c = Coffee(name=coffee['name'], coffee=coffee['coffee'],
               milk=coffee['milk'], water=coffee['water'])
    db.session.add(c)
db.session.commit()

with open('tank_types.json') as f:
    tank_json = json.load(f)

for tank in tank_json:
    t = Tank(name=tank['name'], capacity=tank['capacity'],
             current_amount=tank['current_amount'])
    db.session.add(t)
db.session.commit()

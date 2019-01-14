from coffeeMaker.models import Coffee, Tank
from coffeeMaker.utils import make_coffee


def test_make_all_coffee(session):
    init_coffee(session)
    init_tanks(session)
    beans_lvl = 7 * 9
    water_lvl = 90 + 7 * 30
    milk_lvl = 420
    grounds_lvl = 0

    beans_tank = Tank.query.filter(Tank.name == 'Beans Tank').first()
    water_tank = Tank.query.filter(Tank.name == 'Water Tank').first()
    milk_tank = Tank.query.filter(Tank.name == 'Milk Tank').first()
    grounds_tank = Tank.query.filter(Tank.name == 'Grounds Tank').first()

    beans_tank.current_amount = beans_lvl
    water_tank.current_amount = water_lvl
    milk_tank.current_amount = milk_lvl
    session.commit()

    def usage(c_name):
        c = Coffee.query.filter(Coffee.name == c_name).first()
        beans_per_coffee = 9
        water_per_coffee = 30
        grounds_per_coffee = 9
        nonlocal beans_lvl, water_lvl, grounds_lvl, milk_lvl
        beans_lvl -= c.coffee * beans_per_coffee
        water_lvl -= c.coffee * water_per_coffee + c.water
        milk_lvl -= c.milk
        grounds_lvl += c.coffee * grounds_per_coffee

    assert make_coffee("Espresso") is True
    usage("Espresso")
    assert beans_tank.current_amount == beans_lvl
    assert water_tank.current_amount == water_lvl
    assert milk_tank.current_amount == milk_lvl
    assert grounds_tank.current_amount == grounds_lvl

    assert make_coffee("Caffè latte") is True
    usage("Caffè latte")
    assert beans_tank.current_amount == beans_lvl
    assert water_tank.current_amount == water_lvl
    assert milk_tank.current_amount == milk_lvl
    assert grounds_tank.current_amount == grounds_lvl

    assert make_coffee("Caffè americano") is True
    usage("Caffè americano")
    assert beans_tank.current_amount == beans_lvl
    assert water_tank.current_amount == water_lvl
    assert milk_tank.current_amount == milk_lvl
    assert grounds_tank.current_amount == grounds_lvl

    assert make_coffee("Cappuccino") is True
    usage("Cappuccino")
    assert beans_tank.current_amount == beans_lvl
    assert water_tank.current_amount == water_lvl
    assert milk_tank.current_amount == milk_lvl
    assert grounds_tank.current_amount == grounds_lvl


def test_not_enough_ingredients(session):
    init_coffee(session)
    init_tanks(session)
    beans_lvl = 100
    water_lvl = 500
    milk_lvl = 500

    beans_tank = Tank.query.filter(Tank.name == 'Beans Tank').first()
    water_tank = Tank.query.filter(Tank.name == 'Water Tank').first()
    milk_tank = Tank.query.filter(Tank.name == 'Milk Tank').first()
    grounds_tank = Tank.query.filter(Tank.name == 'Grounds Tank').first()

    beans_tank.current_amount = beans_lvl
    assert make_coffee("Espresso") == 'Not enough Water in the Tank'
    assert beans_tank.current_amount == beans_lvl
    assert water_tank.current_amount == 0
    assert grounds_tank.current_amount == 0

    water_tank.current_amount = water_lvl
    assert make_coffee("Caffè latte") == 'Not enough Milk in the Tank'
    assert beans_tank.current_amount == beans_lvl
    assert water_tank.current_amount == water_lvl
    assert milk_tank.current_amount == 0
    assert grounds_tank.current_amount == 0

    water_tank.current_amount = water_lvl
    milk_tank.current_amount = milk_lvl
    beans_tank.current_amount = 7
    assert make_coffee("Caffè latte") == 'Not enough Coffee Beans in the Tank'
    assert beans_tank.current_amount == 7
    assert water_tank.current_amount == water_lvl
    assert milk_tank.current_amount == milk_lvl
    assert grounds_tank.current_amount == 0


def init_tanks(session):
    tanks = [
        {"name": "Water Tank", "capacity": 1000, "current_amount": 0},
        {"name": "Beans Tank", "capacity": 500, "current_amount": 0},
        {"name": "Grounds Tank", "capacity": 200, "current_amount": 0},
        {"name": "Milk Tank", "capacity": 500, "current_amount": 0}]
    for tank in tanks:
        t = Tank(name=tank['name'], capacity=tank['capacity'],
                 current_amount=tank['current_amount'])
        session.add(t)
    session.commit()


def init_coffee(session):
    coffee_types = [
        {"name": "Espresso", "coffee": 1, "milk": 0, "water": 0},
        {"name": "Caffè latte", "coffee": 2, "milk": 300, "water": 0},
        {"name": "Caffè americano", "coffee": 2, "milk": 0, "water": 90},
        {"name": "Cappuccino", "coffee": 2, "milk": 120, "water": 0}]
    for coffee in coffee_types:
        c = Coffee(name=coffee['name'], coffee=coffee['coffee'],
                   milk=coffee['milk'], water=coffee['water'])
        session.add(c)
    session.commit()

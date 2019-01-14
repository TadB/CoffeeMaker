from coffeeMaker.models import Tank
from coffeeMaker.utils import refill


def init_tanks(session):
    tanks = [
        {"name": "Water Tank", "capacity": 1000, "current_amount": 300},
        {"name": "Beans Tank", "capacity": 500, "current_amount": 300},
        {"name": "Grounds Tank", "capacity": 200, "current_amount": 100},
        {"name": "Milk Tank", "capacity": 500, "current_amount": 300}]
    for tank in tanks:
        t = Tank(name=tank['name'], capacity=tank['capacity'],
                 current_amount=tank['current_amount'])
        session.add(t)
    session.commit()


def test_tank_overfill(session):
    init_tanks(session)

    beans_tank = Tank.query.filter(Tank.name == 'Beans Tank').first()
    beans_tank_start_lvl = beans_tank.current_amount
    water_tank = Tank.query.filter(Tank.name == 'Water Tank').first()
    water_tank_start_lvl = water_tank.current_amount
    milk_tank = Tank.query.filter(Tank.name == 'Milk Tank').first()
    milk_tank_start_lvl = milk_tank.current_amount
    grounds_tank = Tank.query.filter(Tank.name == 'Grounds Tank').first()
    grounds_tank_start_lvl = grounds_tank.current_amount

    assert refill("Water Tank", 1200) == \
        "You are trying to overfill the Water Tank. Nice try."
    assert refill("Beans Tank", 700) == \
        "You are trying to overfill the Beans Tank. Nice try."
    assert refill("Milk Tank", 501) == \
        "You are trying to overfill the Milk Tank. Nice try."
    assert refill("Grounds Tank", 200) == "You are trying to add more Grounds."
    # check if refill function dont change data
    assert beans_tank.current_amount == beans_tank_start_lvl
    assert water_tank.current_amount == water_tank_start_lvl
    assert grounds_tank.current_amount == grounds_tank_start_lvl
    assert milk_tank.current_amount == milk_tank_start_lvl


def test_tank_refill_successfully(session):
    init_tanks(session)
    beans_tank = Tank.query.filter(Tank.name == 'Beans Tank').first()
    water_tank = Tank.query.filter(Tank.name == 'Water Tank').first()
    milk_tank = Tank.query.filter(Tank.name == 'Milk Tank').first()
    grounds_tank = Tank.query.filter(Tank.name == 'Grounds Tank').first()

    assert refill("Water Tank", 1000) == "Water Tank refilled successfuly!"
    assert water_tank.current_amount == 1000
    assert refill("Milk Tank", 500) == "Milk Tank refilled successfuly!"
    assert milk_tank.current_amount == 500
    assert refill("Beans Tank", 500) == "Beans Tank refilled successfuly!"
    assert beans_tank.current_amount == 500
    assert refill("Grounds Tank", 0) == "Grounds Tank refilled successfuly!"
    assert grounds_tank.current_amount == 0


def test_negative_value(session):
    init_tanks(session)

    beans_tank = Tank.query.filter(Tank.name == 'Beans Tank').first()
    beans_tank_start_lvl = beans_tank.current_amount
    water_tank = Tank.query.filter(Tank.name == 'Water Tank').first()
    water_tank_start_lvl = water_tank.current_amount
    milk_tank = Tank.query.filter(Tank.name == 'Milk Tank').first()
    milk_tank_start_lvl = milk_tank.current_amount
    grounds_tank = Tank.query.filter(Tank.name == 'Grounds Tank').first()
    grounds_tank_start_lvl = grounds_tank.current_amount

    assert refill("Water Tank", -1) == 'Negative value is forbidden'
    assert water_tank.current_amount == water_tank_start_lvl
    assert refill("Milk Tank", -1) == 'Negative value is forbidden'
    assert milk_tank.current_amount == milk_tank_start_lvl
    assert refill("Beans Tank", -1) == 'Negative value is forbidden'
    assert beans_tank.current_amount == beans_tank_start_lvl
    assert refill("Grounds Tank", -1) == 'Negative value is forbidden'
    assert grounds_tank.current_amount == grounds_tank_start_lvl


def test_no_need_for_refill(session):
    init_tanks(session)
    grounds_tank = Tank.query.filter(Tank.name == 'Grounds Tank').first()
    grounds_tank.current_amount = 0
    grounds_tank_start_lvl = grounds_tank.current_amount

    assert refill("Grounds Tank", 0) == \
        'Grounds level at minimum - no need for refill'
    assert grounds_tank.current_amount == grounds_tank_start_lvl

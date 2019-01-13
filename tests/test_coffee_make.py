from coffeeMaker.models import Coffee, Tank
from coffeeMaker.utils import make_coffee


def test_make_espresso(session):
    espresso = Coffee(name='Espresso', coffee=1, milk=0, water=0)
    session.add(espresso)
    session.commit()

    init_tanks(session)
    beans_tank = Tank.query.filter(Tank.name == 'Beans Tank').first()
    water_tank = Tank.query.filter(Tank.name == 'Water Tank').first()
    grounds_tank = Tank.query.filter(Tank.name == 'Grounds Tank').first()

    beans_tank.current_amount = 30
    water_tank.current_amount = 100

    assert make_coffee("Espresso") is True
    assert beans_tank.current_amount == 21
    assert water_tank.current_amount == 70
    assert grounds_tank.current_amount == 9


def test_water_empty(session):
    espresso = Coffee(name='Espresso', coffee=1, milk=0, water=0)
    session.add(espresso)
    session.commit()
    init_tanks(session)

    beans_tank = Tank.query.filter(Tank.name == 'Beans Tank').first()
    water_tank = Tank.query.filter(Tank.name == 'Water Tank').first()
    grounds_tank = Tank.query.filter(Tank.name == 'Grounds Tank').first()

    beans_tank.current_amount = 30

    assert make_coffee("Espresso") == 'Not enough Water in the Tank'
    assert beans_tank.current_amount == 30
    assert water_tank.current_amount == 0
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

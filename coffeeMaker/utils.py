from coffeeMaker import db
from coffeeMaker.models import Coffee, Tank


def make_coffee(c_name):
    coffee = Coffee.query.filter(Coffee.name == c_name).first()
    water_tank = Tank.query.filter(Tank.name == 'Water Tank').first()
    milk_tank = Tank.query.filter(Tank.name == 'Milk Tank').first()
    grounds_tank = Tank.query.filter(Tank.name == 'Grounds Tank').first()
    beans_tank = Tank.query.filter(Tank.name == 'Beans Tank').first()

    water_need = coffee.coffee * 30 + coffee.water
    beans_need = coffee.coffee * 9
    grounds_expected = beans_need   # grounds expectation may change in future
    grounds_lvl_expected = grounds_tank.current_amount + grounds_expected
    # resources availability validation
    if water_tank.current_amount < water_need:
        return f'Not enough Water in the Tank'
    elif milk_tank.current_amount < coffee.milk:
        return f'Not enough Milk in the Tank'
    elif beans_tank.current_amount < beans_need:
        return f'Not enough Coffee Beans in the Tank'
    elif grounds_lvl_expected > grounds_tank.capacity:
        return f'Refill Grounds Tank'
        # "can't make this coffee, please refill tanks"
    # resources available - preparing coffee
    beans_tank.current_amount -= beans_need
    water_tank.current_amount -= water_need
    grounds_tank.current_amount += grounds_expected
    milk_tank.current_amount -= coffee.milk

    db.session.commit()
    # print(f"enjoy your delicious {coffee.name} :)")
    return True


def refill(t_name, amount):
    if isinstance(int, amount):
        tank = Tank.query.filter(Tank.name == t_name).first()
        # check if amount fit to empty space
        if amount <= tank.capacity - tank.current_amount:
            tank.current_amount += amount
            db.session.commit()
            return True
    return False


def full_refill(t_name):
    tank = Tank.query.filter(Tank.name == t_name).first()
    if t_name == 'Grounds Tank':
        if tank.current_amount == 0:
            return False
        tank.current_amount = 0
    else:
        if tank.current_amount == tank.capacity:
            return False
        tank.current_amount = tank.capacity
    db.session.commit()
    return True

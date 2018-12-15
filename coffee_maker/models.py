from coffee_maker import db


class Coffee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    coffee = db.Column(db.Integer)
    milk = db.Column(db.Integer)
    water = db.Column(db.Integer)

    def __repr__(self):
        return f'<Coffee {self.name}>'


class Tank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    capacity = db.Column(db.Integer)
    current_amount = db.Column(db.Integer)
    is_needful = db.Column(db.bool)

    def __repr__(self):
        return f'<{self.name} Tank, Current amount: {self.current_amount}>'

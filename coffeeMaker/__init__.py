from flask import Flask
from coffeeMaker.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    return app


from coffeeMaker import models, routes

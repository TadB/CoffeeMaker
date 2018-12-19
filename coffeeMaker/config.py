import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'coffee.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'd783930667b00826b9f9679a3f4cd622'

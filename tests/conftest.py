import pytest
from coffeeMaker import create_app, db as _db
import os


basedir = os.path.abspath(os.path.dirname(__file__))
TESTDB_PATH = os.path.join(basedir, 'test.db')
TEST_DATABASE_URI = 'sqlite:///' + TESTDB_PATH


@pytest.fixture(scope='session')
def app(request):
    settings_override = {
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': TEST_DATABASE_URI
    }
    app = create_app(settings_override)
    # Establish an application context before tests
    app_context = app.app_context()
    app_context.push()

    def tearDown():
        app_context.pop()

    request.addfinalizer(tearDown)
    return app


@pytest.fixture(scope='session')
def db(app, request):
    if os.path.exists(TESTDB_PATH):
        os.unlink(TESTDB_PATH)

    def tearDown():
        _db.drop_all()

    _db.app = app
    _db.create_all()

    request.addfinalizer(tearDown)
    return _db


@pytest.fixture(scope='function')
def session(db, request):
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def tearDown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(tearDown)
    return session

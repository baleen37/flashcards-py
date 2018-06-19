import pytest

from flashcards.application import create_app, get_config
from flashcards.database import dal as _dal


@pytest.fixture(scope='session')
def app():
    app = create_app(get_config('flashcards.config.Testing'))
    ctx = app.app_context()
    ctx.push()

    yield app

    ctx.pop()


@pytest.fixture(scope='session')
def dal(app):
    _dal.setup(app.config['SQLALCHEMY_DATABASE_URI'])
    _dal.create_all()

    yield _dal

    _dal.drop_all()


@pytest.fixture
def db_session(dal):
    connection = dal.engine.connect()
    dal.create_all()

    transaction = connection.begin()
    session = dal.create_session()

    yield session

    transaction.rollback()
    session.commit()
    dal.drop_all()
    connection.close()
    session.remove()


@pytest.fixture
def default_settings(db_session):
    return None

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
    _dal.drop_all()
    _dal.create_all()

    yield _dal

    _dal.drop_all()


@pytest.fixture
def db_session(dal):
    dal.create_all()

    session = dal.create_session()

    yield session

    session.close()
    dal.drop_all()


@pytest.fixture
def default_settings(db_session):
    return None

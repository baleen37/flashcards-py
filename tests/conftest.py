import pytest

from flashcards.application import create_app, get_config
from flashcards.database import dal as _dal

from tests.fixtures.user import *  # noqa


@pytest.fixture
def app():
    app = create_app(get_config('flashcards.config.Testing'))
    ctx = app.app_context()
    ctx.push()

    yield app

    ctx.pop()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def dal(app):
    _dal.setup(app.config['SQLALCHEMY_DATABASE_URI'])
    _dal.create_all()

    yield _dal

    _dal.drop_all()


@pytest.fixture
def db_session(request, dal):
    dal.create_all()

    session = dal.create_session()

    def fn():
        session.close()
        dal.drop_all()

    request.addfinalizer(fn)

    return session


@pytest.fixture
def default_settings(db_session):
    return None

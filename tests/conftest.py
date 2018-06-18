import pytest

from flashcards.application import create_app, get_config
from flashcards.database import dal


@pytest.fixture
def teardown_db():
    pass


@pytest.fixture
def app():
    app = create_app(get_config('flashcards.config.Testing'))
    with app.app_context():
        dal.create_all()
        yield app
        dal.drop_all()


@pytest.fixture(scope='session')
def test_client(app):
    return app.test_client()

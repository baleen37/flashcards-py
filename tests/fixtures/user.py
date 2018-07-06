import pytest

from flashcards.models.user import User
from flashcards.utils.auth import generate_hash_password


@pytest.fixture
def user(db_session):
    user = User(
        username='test_username',
        _password=generate_hash_password('password')
    )
    db_session.add(user)
    db_session.commit()

    return user


class AuthActions:
    def __init__(self, client):
        self._client = client

    def login(self, username='test_username', password='password'):
        return self._client.post(
            '/users/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/users/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)
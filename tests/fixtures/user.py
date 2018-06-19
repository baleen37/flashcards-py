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
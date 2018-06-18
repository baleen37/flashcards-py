import bcrypt
import pytest

from flashcards.core.user import hash_password, is_correct_password


@pytest.mark.parametrize('password', [
    'aaaaaaaaaaaaaaaaaaaaaaaa',
    'bbbbbbbbbbbbbbbbbbbbbbbb',
])
def test_hash_password(password):
    hashed_password = hash_password(password.encode())
    assert bcrypt.hashpw(password.encode(), hashed_password) == hashed_password


@pytest.mark.parametrize('password', [
    'aaaaaaaaaaaaaaaaaaaaaaaa',
    'bbbbbbbbbbbbbbbbbbbbbbbb',
])
def test_is_correct_password(password):
    assert is_correct_password(password.encode(), hash_password(password.encode()))

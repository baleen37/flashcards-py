import flask as fl
from flashcards.core.exceptions import UnauthorizedError
from flashcards.utils.auth import encode_jwt


def test_inject_user(app, client, user):
    encoded = encode_jwt({'username': user.username}, app.config['SECRET_KEY'])
    res = client.get('/', headers={'Authorization': f'Bearer {encoded.decode()}'})
    assert res.status_code == 200

    assert fl.g.user.username == user.username


def test_inject_user_failure(app):
    res = app.test_client().get('/', headers={'Authorization': 'Bearer NONE'})
    assert res.status_code == UnauthorizedError.status_code

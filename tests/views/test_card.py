import pytest

from flashcards.core.exceptions import UnauthorizedError
from tests.fixtures.user import AuthActions


def test_login_required_card_list(app, user, auth: AuthActions):
    auth.login(username=user.username, password='password')
    res = app.test_client().get('/cards/')

    assert res.status_code == 200


def test_login_required_card_list_failure(app, user, auth: AuthActions):
    res = app.test_client().get('/cards/')

    assert res.status_code == UnauthorizedError.status_code


def test_card_list(app):
    res = app.test_client().get('/cards')

    assert res.status_code == 200

    json_data = res.get_json()
    assert json_data['data']['cards']


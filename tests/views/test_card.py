import pytest


def test_card_list(app):
    res = app.test_client().get('/cards')

    assert res.status_code == 200

    json_data = res.get_json()
    assert json_data['data']['cards']


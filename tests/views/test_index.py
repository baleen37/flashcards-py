import pytest


def test_index(app, default_settings):
    res = app.test_client().get( '/', )
    assert res.status_code == 200

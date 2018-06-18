import sys


def test_python_version():
    assert 3 == sys.version_info.major
    assert 6 == sys.version_info.minor
    assert 2 <= sys.version_info.micro


def test_testing_mode(app):
    assert app.config['TESTING']


def test_index(app):
    res = app.test_client().get('/')
    assert res.status_code == 200

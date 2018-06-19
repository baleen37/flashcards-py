import pytest


@pytest.mark.parametrize('username', ['aaaaaaaa', 'bbbbbb'])
@pytest.mark.parametrize('password', ['AAAAAAAA', 'BBBBBB'])
def test_register(app, username, password, default_settings):
    res = app.test_client().post(
        '/users/register',
        data={
            'username': username,
            'password': password
        }
    )
    assert res.status_code == 200

    json_data = res.get_json()
    data = json_data['data']
    assert data['username'] == username


def test_login(app, user, default_settings):
    res = app.test_client().post(
        '/users/login',
        data={
            'username': user.username,
            'password': 'password'
        }
    )
    assert res.status_code == 200

    json_data = res.get_json()
    assert json_data['data']['token']
    assert json_data['data']['username'] == user.username

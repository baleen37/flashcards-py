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

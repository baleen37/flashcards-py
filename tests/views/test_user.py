import pytest


@pytest.mark.parametrize('username', ['aaaaaaaa', 'bbbbbb'])
@pytest.mark.parametrize('password', ['AAAAAAAAAA', 'BBBBBB'])
def test_register(app, username, password):
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
    assert data['user']['username'] == username

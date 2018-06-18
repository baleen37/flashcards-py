import pytest


@pytest.mark.parametrize('username', ['aaaaaaaa', 'bbbbbb'])
def test_register(app, username):
    res = app.test_client().post(
        '/users/register',
        data={
            'username': username,
            'password': '1234'
        }
    )
    json_data = res.get_json()
    data = json_data['data']
    assert data['user']['username'] == username

import flask as fl

from flashcards.core.api import APIResponse
from flashcards.core.exceptions import APIException
from flashcards.core.user import UserRegistrationInfo, LoginUserInfo
from flashcards.database import dal
from flashcards.services.auth import RegistrationService, LoginService

bp = fl.Blueprint('user', __name__, url_prefix='/users')


@bp.route('/register', methods=['POST'])
def register():
    username = fl.request.form.get('username')
    password = fl.request.form.get('password')

    try:
        user_info = UserRegistrationInfo(
            username=username,
            password=password)
        rs = RegistrationService(dal.session)
        user = rs.register(user_info)

        return APIResponse(data={
            'username': user.username,
        })
    except Exception as e:
        raise APIException(e)


@bp.route('/login', methods=['POST'])
def login():
    username = fl.request.form.get('username')
    password = fl.request.form.get('password')

    try:
        user_info = LoginUserInfo(username=username, password=password)
        ls = LoginService(dal.session, secret_key=fl.current_app.config['SECRET_KEY'])
        token = ls.login(user_info)

        return APIResponse(data={
            'username': token.user.username,
            'token': token.token.decode('utf-8')
        })
    except Exception as e:
        raise APIException(e, status_code=401)



@bp.route('/logout')
def logout():
    return ''

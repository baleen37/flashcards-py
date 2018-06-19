import flask as fl

from flashcards.core.api import APIResponse
from flashcards.core.exceptions import APIException
from flashcards.core.user import UserRegistrationInfo
from flashcards.database import dal
from flashcards.services.auth import RegistrationService

bp = fl.Blueprint('user', __name__, url_prefix='/users')


@bp.route('/register', methods=['POST'])
def register():
    username = fl.request.form['username']
    password = fl.request.form['password']
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
        dal.session.rollback()
        raise APIException(e)


@bp.route('/login', methods=['POST'])
def login():
    return ''


@bp.route('/logout')
def logout():
    return ''

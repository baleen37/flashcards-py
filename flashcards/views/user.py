import flask as fl

from flashcards.core.api import APIResponse
from flashcards.database import dal
from flashcards.exc.api import APIException
from flashcards.models.users import User

bp = fl.Blueprint('user', __name__, url_prefix='/users')


@bp.route('/register', methods=['POST'])
def register():
    username = fl.request.form['username']
    password = fl.request.form['password']
    if dal.session.query(User).filter(User.username == username).scalar():
        raise APIException('already exists username')
    try:
        user = User(username=username)
        user.password = password
        dal.session.add(user)
        dal.session.commit()

        return APIResponse(data={
            'user': {
                'username': username,
            }
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

import flask as fl

from flashcards.database import session
from flashcards.exc.api import APIException
from flashcards.models.users import User

bp = fl.Blueprint('user', __name__)


@bp.route('/register', methods=['POST'])
def register():
    username = fl.request.form['username']
    password = fl.request.form['password']
    if session.query(User).filter(User.username == username).scalar():
        raise Exception()
    try:
        user = User(username=username)
        user.password = password
        session.add(user)
        session.commit()

        return
    except Exception as e:
        session.rollback()
        return APIException(e)


@bp.route('/login', methods=['POST'])
def login():
    return ''


@bp.route('/logout')
def logout():
    return ''

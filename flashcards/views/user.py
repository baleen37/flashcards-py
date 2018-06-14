import flask as fl

bp = fl.Blueprint('user', __name__)


@bp.route('/')
def index():
    return ''

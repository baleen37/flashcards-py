import flask as fl

bp = fl.Blueprint('index', __name__)


@bp.route('/')
def index():
    return ''
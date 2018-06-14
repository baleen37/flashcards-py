import flask as fl

bp = fl.Blueprint('main', __name__)


@bp.route('/')
def index():
    return fl.render_template('index.jinja2')

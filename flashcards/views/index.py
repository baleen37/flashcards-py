import flask as fl

from flashcards.core.api import APIResponse

bp = fl.Blueprint('index', __name__)


@bp.route('/')
def index():
    return APIResponse(
        data={'hi': 's'},
        message='ok',
        status=200
    )

import flask as fl

from flashcards.core.api import APIResponse
from flashcards.core.exceptions import APIException
from flashcards.utils.auth import login_required

bp = fl.Blueprint('card', __name__, url_prefix='/cards')


@bp.route('/')
@login_required
def index():
    try:
        return APIResponse(data={
            'cards': []
        })
    except Exception as e:
        raise APIException(e)

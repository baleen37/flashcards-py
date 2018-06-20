import flask as fl

from flashcards.core.api import APIResponse
from flashcards.core.exceptions import APIException
from flashcards.database import dal
from flashcards.models.card import Card

bp = fl.Blueprint('card', __name__, url_prefix='/cards')


@bp.route('/', methods=['GET'])
def index():
    try:
        cards = dal.session.query(Card).filter(Card.user_id == 1).all()

        return APIResponse(data={
            'cards': []
        })
    except Exception as e:
        raise APIException(e)
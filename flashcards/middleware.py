import flask as fl

from flashcards.core.api import APIResponse
from flashcards.database import dal
from flashcards.exc.api import APIException


@fl.current_app.teardown_request
def shutdown_session(exception=None):
    dal.session.remove()


@fl.current_app.errorhandler(APIException)
def handle_invalid_usage(error):
    response = APIResponse(
        message=error.message,
        status=error.status_code or 500
    )
    return response

import flask as fl

from flashcards.core.api import APIResponse
from flashcards.database import session


@fl.current_app.teardown_request
def shutdown_session(exception=None):
    session.remove()


@fl.current_app.errorhandler
def handle_invalid_usage(error):
    response = APIResponse(
        message=error.to_dict(),
        status=error.status_code
    )
    return response

import flask as fl
import jwt

from flashcards.core.api import APIResponse
from flashcards.core.exceptions import APIException, ValidationError, FlashcardsError, UnauthorizedError
from flashcards.core.user import ContextUserInfo
from flashcards.database import dal


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


@fl.current_app.errorhandler(FlashcardsError)
def handle_custom_error(error):
    response = APIResponse(
        message=str(error),
        status=getattr(error, 'status_code', 500)
    )
    return response


@fl.current_app.before_request
def inject_user():
    authorization = fl.request.headers.get('Authorization')
    if authorization:
        schema, credentials = authorization.split(' ', 1)
        if schema == 'Bearer':
            key = fl.current_app.config.get('SECRET_KEY')
            try:
                encoded_jwt = jwt.decode(credentials, key)
                username = encoded_jwt['username']
                fl.g.user = ContextUserInfo(username=username)
            except jwt.DecodeError as e:
                raise UnauthorizedError('Not enough segments')


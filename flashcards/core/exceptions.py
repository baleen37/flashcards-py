class FlashcardsError(Exception):
    status_code = 500


class APIException(FlashcardsError):
    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if not status_code:
            self.status_code = status_code
        self.payload = payload


class UnauthorizedError(FlashcardsError):
    status_code = 401


class ValidationError(FlashcardsError):
    pass


class PersistenceError(FlashcardsError):
    pass

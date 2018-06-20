from flashcards.models.user import User


class DataInfo:
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)


class ContextUserInfo(DataInfo):
    username = None


class UserRegistrationInfo(DataInfo):
    username = None
    password = None


class LoginUserInfo(DataInfo):
    username = None
    password = None


class AuthTokenInfo(DataInfo):
    user: User = None
    token: str = None


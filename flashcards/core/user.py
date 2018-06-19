import bcrypt
import jwt


class UserRegistrationInfo:
    username = None
    password = None

    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)


class DataInfo:
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)


class UserRegistrationInfo(DataInfo):
    username = None
    password = None


class LoginUserInfo(DataInfo):
    username = None
    password = None

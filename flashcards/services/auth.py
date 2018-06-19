import jwt

from flashcards.core.exceptions import PersistenceError, ValidationError
from flashcards.core.user import LoginUserInfo
from flashcards.models.user import User
from flashcards.utils.auth import generate_hash_password, is_correct_password


class RegistrationService:

    def __init__(self, db_session):
        self.db_session = db_session

    def register(self, user_info):

        try:
            self._validate(user_info)
        except Exception as e:
            raise

        user = self._store_user(user_info)
        return user

    def _validate(self, user_info):
        if not user_info.username:
            raise ValidationError('Required username')

        if not user_info.password:
            raise ValidationError('Required password')

        if self.db_session.query(User).filter(User.username == user_info.username).scalar():
            raise ValidationError('Already exists username')

    def _store_user(self, user_info):
        try:
            user = User(
                username=user_info.username,
                password=generate_hash_password(user_info.password.encode()),
            )
            self.db_session.add(user)
            self.db_session.commit()
            return user
        except Exception:
            self.db_session.rollback()
            raise PersistenceError("Could not persist user")


class LoginService:

    def __init__(self, db_session, secret_key):
        assert secret_key, 'Required secret_key'

        self.db_session = db_session
        self.secret_key = secret_key

    def login(self, user_info: LoginUserInfo):
        try:
            self._validate(user_info)

            user = self.db_session.query(User).filter(User.username == user_info.username).scalar()
            if not user:
                raise ValidationError('Not exists user')

            if not is_correct_password(user_info.password.encode(), user.password):
                raise ValidationError('Wrong password')

            return self._generate_token(user)
        except Exception as e:
            raise

    def _validate(self, user_info):
        if not user_info.username:
            raise ValidationError('Required username')

        if not user_info.password:
            raise ValidationError('Required password')

    def _generate_token(self, user: User):
        return jwt.encode({'username': user.username}, self.secret_key)

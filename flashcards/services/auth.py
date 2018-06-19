from flashcards.core.exceptions import PersistenceError, ValidationError
from flashcards.models.user import User
from flashcards.utils.auth import hash_password


class RegistrationService:

    def __init__(self, db_session):
        self.db_session = db_session

    def register(self, user_info):

        try:
            self._validate(user_info)
        except Exception as e:
            print(e)
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
                password=hash_password(user_info.password.encode()),
            )
            self.db_session.add(user)
            self.db_session.commit()
            return user
        except Exception:
            self.db_session.rollback()
            raise PersistenceError("Could not persist user")



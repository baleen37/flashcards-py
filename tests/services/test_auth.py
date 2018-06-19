import pytest

from flashcards.core.exceptions import ValidationError
from flashcards.core.user import UserRegistrationInfo
from flashcards.models.user import User
from flashcards.services.auth import RegistrationService


class TestRegistrationService:

    def test_register(self, db_session):
        user_info = UserRegistrationInfo(
            username='baleen',
            password='testtest',
        )

        self._get_service(db_session).register(
            user_info=user_info)

        actual_user = db_session.query(User).filter(User.username == user_info.username).one()
        assert actual_user.id is not None

    def test_raise_invalidation_error(self, db_session):
        user_info = UserRegistrationInfo(
            username='',
            password='',
        )

        with pytest.raises(ValidationError) as excinfo:
            self._get_service(db_session).register(
                user_info=user_info)

    def _get_service(self, db_session):
        return RegistrationService(db_session)


import pytest

from flashcards.core.exceptions import ValidationError
from flashcards.core.user import UserRegistrationInfo, LoginUserInfo
from flashcards.models.user import User
from flashcards.services.auth import RegistrationService, LoginService


class TestRegistrationService:

    def test_register(self, db_session):
        user_info = UserRegistrationInfo(
            username='baleen',
            password='password',
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


class TestLoginService:

    def test_login(self, app, db_session, user):
        user_info = LoginUserInfo(username=user.username,
                                  password='password')
        self._get_service(app, db_session).login(user_info=user_info)

    def test_login_wrong_params(self, app, db_session, user):
        user_info = LoginUserInfo(username=user.username, password='None')
        with pytest.raises(ValidationError) as excinfo:
            self._get_service(app, db_session).login(user_info)

    def _get_service(self, app, db_session):
        return LoginService(db_session, app.config['SECRET_KEY'])

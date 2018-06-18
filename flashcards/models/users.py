import bcrypt
import sqlalchemy as sa
from sqlalchemy import func

from flashcards.database import Base


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String, nullable=False, unique=True, index=True)
    _password = sa.Column(sa.String, nullable=False)
    created_at = sa.Column(sa.DateTime, nullable=False, server_default=func.now())

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = bcrypt.hashpw(password, bcrypt.gensalt())

    def is_correct_password(self, password):
        return bcrypt.hashpw(password, self._password) == self._password

import sqlalchemy as sa
from sqlalchemy import func

from flashcards.database import Base


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String, nullable=False, unique=True, index=True)
    _password = sa.Column('password', sa.LargeBinary, nullable=False)
    created_at = sa.Column(sa.DateTime, nullable=False, server_default=func.now())

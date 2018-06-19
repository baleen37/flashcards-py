import sqlalchemy as sa
from sqlalchemy import func

from flashcards.database import Base


class Card(Base):
    __tablename__ = 'cards'

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey('users.id'), index=True)
    title = sa.Column('title', sa.String, nullable=False, index=True)
    content = sa.Column('content', sa.Text, nullable=True)
    created_at = sa.Column(sa.DateTime, nullable=False, server_default=func.now(), index=True)


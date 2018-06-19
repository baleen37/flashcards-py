from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, create_session

Base = declarative_base()


# Data Access Layer
class Dal:
    def __init__(self, session=None, engine=None):
        self.session = session
        self.engine = engine

    def setup(self, uri, **kwargs):
        self.engine = create_engine(uri, **kwargs)
        self.session = self.create_session()

    def create_session(self):
        return scoped_session(lambda: create_session(bind=self.engine, autocommit=False))

    def create_all(self):
        from flashcards.models import import_models
        import_models()
        Base.metadata.create_all(bind=self.engine)

    def drop_all(self):
        Base.metadata.drop_all(bind=self.engine)


dal = Dal()

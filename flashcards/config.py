class Config:
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost:5432/postgres'


class Development(Config):
    pass


class Production(Config):
    pass


class Testing(Config):
    Testing = True

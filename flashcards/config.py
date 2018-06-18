class Config:
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres:postgres@localhost:5432/postgres'


class Development(Config):
    DEBUG = True


class Production(Config):
    PRODUCTION = True


class Testing(Config):
    TESTING = True

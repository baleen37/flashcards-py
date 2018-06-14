import flask as fl

from flashcards.database import init_engine, init_db, db_session


def create_app(config_filename):
    app = fl.Flask(__name__)
    app.config.from_pyfile(config_filename)

    from flashcards.views.index import bp as index_bp
    from flashcards.views.user import bp as user_bp

    app.register_blueprint(index_bp)
    app.register_blueprint(user_bp)

    init_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    init_db()

    # FIXME : for modular
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app

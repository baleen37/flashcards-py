import flask as fl


def create_app(config_filename):
    app = fl.Flask(__name__)
    app.config.from_pyfile(config_filename)

    from flashcards.views.index import bp
    app.register_blueprint(bp)
    return app

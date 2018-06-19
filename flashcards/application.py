from importlib import import_module

import flask as fl

from flashcards.database import dal


def get_config(config_class_string):
    config_module, config_class = config_class_string.rsplit('.', 1)
    config_class_obj = getattr(import_module(config_module), config_class)
    config_obj = config_class_obj()
    return config_obj


def create_app(config_obj):
    app = fl.Flask(__name__)
    app.config.from_object(config_obj)

    from flashcards.views.index import bp as index_bp
    from flashcards.views.user import bp as user_bp

    app.register_blueprint(index_bp)
    app.register_blueprint(user_bp)

    with app.app_context():
        import_module('flashcards.middleware')
        dal.setup(uri=app.config['SQLALCHEMY_DATABASE_URI'])
        dal.create_all()

    return app

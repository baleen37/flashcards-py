from flashcards.application import create_app, get_config


def test_get_config():
    config_obj = get_config('flashcards.config.Testing')
    assert config_obj.Testing




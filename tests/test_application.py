from flashcards.application import get_config


def test_get_config_Development():
    config_obj = get_config('flashcards.config.Development')
    assert config_obj.DEBUG


def test_get_config_Production():
    config_obj = get_config('flashcards.config.Production')
    assert config_obj.PRODUCTION


def test_get_config_Testing():
    config_obj = get_config('flashcards.config.Testing')
    assert config_obj.TESTING




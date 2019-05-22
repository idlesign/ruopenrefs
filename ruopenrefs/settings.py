import envbox

SETTINGS_PREFIX = 'RUOREFS_'

env_all = envbox.get_environment()
env = env_all.getmany(SETTINGS_PREFIX)


def get_setting(name: str) -> str:
    """Возвращает значение указанной настройки (префикс опускается)."""
    value = env.get(name)
    assert value, 'Укажите значение для настройки %s' % ('%s%s' % (SETTINGS_PREFIX, name))
    return value

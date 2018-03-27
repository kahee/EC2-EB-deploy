import os

# DJANGO_SETTINGS_MODULE이  config.settings 기본 실행이 되면 __ini__
# export 선언 안하고 사용할 수 있게 한 것
SETTINGS_MODULE = os.environ.get('DJANGO_SETTINGS_MODULE')
if not SETTINGS_MODULE or SETTINGS_MODULE == 'config.settings':
    from .local import *

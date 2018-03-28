from .base import *

secrets_base = json.loads(open(SECRET_DEV, 'rt').read())
# set_config(secrets_base, module_name=__name__, start=False)

DATABASES = secrets_base['DATABASES']

INSTALLED_APPS += [
    'django_extensions',
    'storages',
]

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '.amazonaws.com',
    '.elasticbeanstalk.com',
]

# Media(user-uploaded file)을 위한 스토리지
DEFAULT_FILE_STORAGE = 'config.storage.DefaultFileStorage'
# Static files(collectstatic) 을 위한 스토리지
STATICFILES_STORAGE = 'config.storage.StaticFileStorage'

WSGI_APPLICATION = 'config.wsgi.dev.application'

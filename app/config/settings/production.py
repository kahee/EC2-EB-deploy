from .base import *
secrets_base = json.loads(open(SECRET_PRODUCTION, 'rt').read())

DATABASES = secrets_base['DATABASES']
DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '.amazonaws.com',
]

# Media(user-uploaded file)을 위한 스토리지
DEFAULT_FILE_STORAGE = 'config.storage.DefaultFileStorage'
# Static files(collectstatic) 을 위한 스토리지
STATICFILES_STORAGE = 'config.storage.StaticFileStorage'

WSGI_APPLICATION = 'config.wsgi.production.application'

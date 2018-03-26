from .base import *

secrets_base = json.loads(open(SECRET_DEV, 'rt').read())
set_config(secrets_base, module_name=__name__, start=False)

# ALLOWED_HOSTS = []

# WSGI_APPLICATION = 'config.wsgi.local.application'

INSTALLED_APPS += [
    'django_extensions',
]

DEBUG = True

ALLOWED_HOSTS = [
    '.amazonaws.com',
    'localhost',
]
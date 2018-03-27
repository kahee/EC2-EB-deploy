from .base import *
secrets_base = json.loads(open(SECRET_DEV, 'rt').read())
# set_config(secrets_base, module_name=__name__, start=False)

DATABASES = secrets_base['DATABASES']

INSTALLED_APPS += [
    'django_extensions',
]

DEBUG = True

ALLOWED_HOSTS = [
    '.amazonaws.com',
    'localhost',
]

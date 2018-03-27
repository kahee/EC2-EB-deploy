from .base import *

secrets_base = json.loads(open(SECRET_LOCAL, 'rt').read())

DATABASES = secrets_base['DATABASES']
INSTALLED_APPS += [
    'django_extensions',
]

DEBUG = True
ALLOWED_HOSTS = [
    '.amazonaws.com',
    'localhost',
]


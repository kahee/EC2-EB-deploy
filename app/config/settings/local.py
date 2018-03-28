from .base import *

secrets_base = json.loads(open(SECRET_LOCAL, 'rt').read())


INSTALLED_APPS += [
    'django_extensions',
]

DEBUG = True
ALLOWED_HOSTS = [
    '.amazonaws.com',
    'localhost',
    '127.0.0.1',
]


WSGI_APPLICATION = 'config.wsgi.local.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

from .base import *
secrets_base = json.loads(open(SECRET_PRODUCTION, 'rt').read())

DATABASES = secrets_base['DATABASES']
DEBUG = False

ALLOWED_HOSTS = [
    '.amazonaws.com',
]

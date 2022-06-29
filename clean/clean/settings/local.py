from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

WSGIT_APPLICATION = 'clean.wsgi.local.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }

}

AUTH_PASSWORD_VALIDATORS = [

]

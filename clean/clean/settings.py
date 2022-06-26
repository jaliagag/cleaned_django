#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
STATICFILES_DIRS = (  os.path.join(BASE_DIR, 'static'),)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE","jaliagaSite.settings")
application = get_wsgi_application()
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)


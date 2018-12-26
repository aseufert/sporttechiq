import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "sporttech_db",
        'USER': "postgres",
        'PASSWORD': "seuf86",
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Amazon S3
AWS_ACCESS_KEY_ID = 'AKIAIQRDDXK34ZRTG56A'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'sporttech-staging'
AWS_S3_CUSTOM_DOMAIN = 'd1kpiwu2hgqz6c.cloudfront.net'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'sporttech/static'),
]

CLOUD_FRONT_CUSTOM_DOMAIN = 'd1kpiwu2hgqz6c.cloudfront.net'
STATIC_URL = '//{}/{}/'.format(CLOUD_FRONT_CUSTOM_DOMAIN, AWS_LOCATION)

# S3 Media - Handled by another instance
DEFAULT_FILE_STORAGE = 'sporttech.settings.storage_backends.MediaStorage'
# used to collectstatic to S3 bucket
STATICFILES_STORAGE = 'sporttech.settings.storage_backends.StaticStorage'

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://localhost:8000/'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sporttech.settings.dev")

INSTALLED_APPS += [
    'debug_toolbar'
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

try:
    from .local import *
except ImportError:
    pass
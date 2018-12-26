import os
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Amazon S3
AWS_ACCESS_KEY_ID = 'AKIAIQRDDXK34ZRTG56A'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'sporttech-staging'
AWS_S3_CUSTOM_DOMAIN = 'd1kpiwu2hgqz6c.cloudfront.net'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
# Set this 12/26/18 based on this SO
# https://stackoverflow.com/questions/6618013/django-staticfiles-and-amazon-s3-how-to-detect-modified-files?rq=1
# Need to test and put into production
AWS_PRELOAD_METADATA = True


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'sporttech/static'),
]

CLOUD_FRONT_CUSTOM_DOMAIN = 'd1kpiwu2hgqz6c.cloudfront.net'
STATIC_URL = '//{}/{}/'.format(CLOUD_FRONT_CUSTOM_DOMAIN, AWS_LOCATION)

# S3 Media - Handled by another instance
DEFAULT_FILE_STORAGE = 'sporttech.settings.storage_backends.MediaStorage'
# used to collectstatic to S3 bucket
STATICFILES_STORAGE = 'sporttech.settings.storage_backends.StaticStorage'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['staging.sporttechiq.com']

# set up for email
ADMINS = (
    ('sporttech_admin', 'noreply@sporttechiq.com'),
)

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': "staging_postgres",
#         'USER': "amseufert",
#         'PASSWORD': "Vertical_Ventures2017",
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# set email server
EMAIL_HOST = 'smtp.webfaction.com'

EMAIL_HOST_USER = 'sporttech_admin'

EMAIL_HOST_PASSWORD = 'P9O876IJhu56hgD'

DEFAULT_FROM_EMAIL = 'noreply@sporttechiq.com'

SERVER_EMAIL = 'noreply@sporttechiq.com'

MAIL_USE_SSL = False


# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'https://staging.sporttechiq.com/'

#uncomment when you figured out the static files issue
# INSTALLED_APPS += [
#     'debug_toolbar'
# ]

# MIDDLEWARE += [
#     'debug_toolbar.middleware.DebugToolbarMiddleware',
# ]

try:
    from .local import *
except ImportError:
    pass

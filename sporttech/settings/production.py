import os
from .base import *


DEBUG = False

ALLOWED_HOSTS = [
    'sporttechiq.com',
    'www.sporttechiq.com',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "prod_postgres",
        'USER': "amseufert",
        'PASSWORD': "5BF-9SJ-Bos-76y",
        'HOST': 'Wf-148-72-160-136.webfaction.com',
        'PORT': '5432',
    }
}

AWS_ACCESS_KEY_ID = 'AKIAIQRDDXK34ZRTG56A'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'sporttech-prod'
AWS_S3_CUSTOM_DOMAIN = 'd30ugx5vrv5w7t.cloudfront.net'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'sporttech/static'),
]

CLOUD_FRONT_CUSTOM_DOMAIN = 'd30ugx5vrv5w7t.cloudfront.net'
STATIC_URL = '//{}/{}/'.format(CLOUD_FRONT_CUSTOM_DOMAIN, AWS_LOCATION)

# S3 Media - Handled by another instance
DEFAULT_FILE_STORAGE = 'sporttech.settings.storage_backends.MediaStorage'
# used to collectstatic to S3 bucket
STATICFILES_STORAGE = 'sporttech.settings.storage_backends.StaticStorage'

# set up for email
ADMINS = (
    ('sporttech_admin', 'noreply@sporttechiq.com'),
)

# set email server
EMAIL_HOST = 'smtp.webfaction.com'

EMAIL_HOST_USER = 'sporttech_admin'

EMAIL_HOST_PASSWORD = 'P9O876IJhu56hgD'

DEFAULT_FROM_EMAIL = 'noreply@sporttechiq.com'

SERVER_EMAIL = 'noreply@sporttechiq.com'

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'https://www.sporttechiq.com'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sporttech.settings.production")

try:
    from .local import *
except ImportError:
    pass
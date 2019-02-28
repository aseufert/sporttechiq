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

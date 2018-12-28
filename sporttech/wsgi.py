"""
WSGI config for sporttech project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
import os
import json

FILE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
site_config = os.path.join(FILE_DIR, 'sporttech', 'settings', 'site_config.json')

with open(site_config) as f:
    configs = json.loads(f.read())

os.environ['DJANGO_SETTINGS_MODULE'] = configs['SETTINGS']

application = get_wsgi_application()

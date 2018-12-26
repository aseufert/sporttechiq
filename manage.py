#!/usr/bin/env python
import os
import sys
import json

if __name__ == "__main__":
    PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    site_config = os.path.join(PROJECT_DIR, 'sporttech', 'sporttech', 'settings', 'site_config.json')

    with open(site_config) as f:
        configs = json.loads(f.read())

    os.environ['DJANGO_SETTINGS_MODULE'] = configs['SETTINGS']

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    import os
    import json
    from django.core.management import execute_from_command_line

    FILE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    site_config = os.path.join(FILE_DIR, 'sporttech','sporttech', 'settings', 'site_config.json')

    with open(site_config) as f:
        configs = json.loads(f.read())

    os.environ['DJANGO_SETTINGS_MODULE'] = configs['SETTINGS']

    execute_from_command_line(sys.argv)

#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
	# setting DJANGO_SETTINGS_MODULE in settings folders instead
	# uncomment is fails
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sporttech.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

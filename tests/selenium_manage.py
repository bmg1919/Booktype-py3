#!/usr/bin/env python
import os
import sys

from pathlib import Path

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "selenium_settings")

    BASE_DIR = Path(os.path.abspath(__file__)).parent

    sys.path.insert(0, str(BASE_DIR))
    sys.path.insert(0, str(BASE_DIR.parent / 'lib'))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

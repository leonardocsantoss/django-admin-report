#!/usr/bin/python
# -*- coding:utf-8 -*-
from django.core.management import execute_manager
import sys
from os.path import join
from django.conf import settings

try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)


sys.path.insert(0, join(settings.PROJECT_ROOT_PATH, "lib"))
sys.path.insert(0, join(settings.PROJECT_ROOT_PATH, "src"))

if __name__ == "__main__":
    execute_manager(settings)

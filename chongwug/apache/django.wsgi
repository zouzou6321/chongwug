import os
import sys

path = '/chongwug/chongwug'
if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'chongwug.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
import os
import sys

path = '/chongwug/petlife'
if path not in sys.path:
    sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'petlife.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
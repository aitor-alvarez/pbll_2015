"""
WSGI config for nflrcpbll project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys
# 
sys.path.insert(0, '/pythonweb/nflrc-pbll-dev/')
# 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nflrcpbll.settings.prod-nflrcpbll-hawaii-edu")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


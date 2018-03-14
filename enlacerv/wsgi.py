"""
WSGI config for enlacerv project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

try:
	import pymysql
	pymysql.install_as_MySQLdb()
except ImportError:
	pass

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "enlacerv.settings")

application = get_wsgi_application()

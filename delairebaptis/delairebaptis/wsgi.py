#this file is how the python web application and the server communicate
# I won't be messing with this file  

"""
WSGI config for delairebaptis project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'delairebaptis.settings')

application = get_wsgi_application()

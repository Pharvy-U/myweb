"""
WSGI config for myweb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import pathlib
import dotenv


BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

dotenv.read_dotenv(BASE_DIR / '.env')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myweb.settings')

application = get_wsgi_application()

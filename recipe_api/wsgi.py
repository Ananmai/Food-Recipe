"""
WSGI config for recipe_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_api.settings')

application = get_wsgi_application()

# Auto-migrate on startup for demo environments
try:
    call_command('migrate', interactive=False)
except Exception as e:
    print(f"Startup migration attempt failed: {e}")

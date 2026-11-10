"""Prepare a read-only database for the UI demo, without customer data."""
import os
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capstone.settings')
os.environ.setdefault('VERCEL_DEMO', 'True')

import django
from django.conf import settings

database = Path(__file__).resolve().parent / 'db.vercel.sqlite3'
settings.DATABASES['default'] = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': database,
}
django.setup()
from django.core.management import call_command
call_command('migrate', interactive=False)

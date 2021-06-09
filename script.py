import os, sys, secrets
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from datetime import datetime
from os import scandir

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    formated_date = d.strftime('%Y-%m-%d %H:%M:%S')
    return formated_date

def get_files():
    dir_entries = scandir('.')
    for entry in dir_entries:
        if entry.is_file():
            hashv = secrets.token_hex(16)
            info = entry.stat()
            name = entry.name
            published = datetime.now()
            created_date = convert_date(info.st_ctime)
            modified_date = convert_date(info.st_mtime)

get_files()
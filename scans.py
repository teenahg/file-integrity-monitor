import os, sys, secrets
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.utils import timezone
from django.db import models

from datetime import datetime
from os import scandir
from app.models import File

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
            try:
                # creates a new instance of file and fills in the current file
                new_file = File(
                    name = name, # file name
                    location = entry.path, # file path
                    hash_value = hashv, # file's created hash value
                    slug = name, # file's slug value(name split with hyphens)
                    publish = created_date,
                    created = created_date,
                    updated = modified_date,
                )
                new_file.save()
            except Exception as e:
                print(e, e.__traceback__, " at line ", e.__traceback__.tb_lineno)
            else:
                print("file saved successfully")


get_files()
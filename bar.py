import os, sys, secrets
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fimtool.settings')
django.setup()

from filemanager.models import Post

the_string = 'the Document, The File, My Name, Corel'
usage = []
edited = the_string.split(', ')
for index, char in enumerate(edited):
    usage.append(char)
    new_post = Post(
        name = usage,
    )
    new_post.save()
    print("file saved")
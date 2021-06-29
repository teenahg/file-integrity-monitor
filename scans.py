import os, sys, hashlib
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from app.models import cFile

def get_files():
        for file in os.scandir('.'):
            if os.path.isfile(file):
                with open(file,'r', encoding="ascii", errors="surrogateescape") as f:
                    data =f.read
                    for chunk in iter(lambda: f.read(2048), ""):
                        myFilesEncoded = str.encode(chunk,encoding="ascii", errors="surrogateescape")
                        hash = hashlib.sha256()
                        hash.update(myFilesEncoded)    
                        sha256 = hash.hexdigest()
                        hashv = sha256
                    info = file.stat()
                    name = file.name
                    try:
                        # creates a new instance of file and fills in the current file
                        new_file = cFile(
                            name = name, # file name
                            location = file.path, # file path
                            hash_value = hashv, # file's created hash value
                            )
                        new_file.save()
                    except Exception as e:
                        print(e, e.__traceback__, " at line ", e.__traceback__.tb_lineno)
                    finally:
                        print("All files have been saved")
get_files()
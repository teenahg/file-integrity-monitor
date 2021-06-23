from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from app.models import File

@login_required(login_url="/login/")
def index(request):
    files = File.objects.all()
    users = User.objects.all()
    context = {'files': files, 'users': users}
    context['segment'] = 'index'
    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    try:    
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
    except template.TemplateDoesNotExist:
        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))
    except:
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def users(request):
    users = User.objects.all()
    context = {'users': users,}
    return render(request, 'users.html', context)

@login_required(login_url="/login/")
def files(request):
    files = File.objects.all()
    context = {'files': files,}
    return render(request, 'files.html', context)

@login_required(login_url="/login/")
def verify(request):
    import os,hashlib,time
    from operator import itemgetter
    stored_files = File.objects.all()
    files = []
    # while True:
    for file in os.listdir('.'):
        if os.path.isfile(file):
            with open(file,'r', encoding="ascii", errors="surrogateescape") as f:
                data = f.read
                for chunk in iter(lambda: f.read(2048), ""):
                    myFilesEncoded = str.encode(chunk,encoding="ascii", errors="surrogateescape")
                    hash = hashlib.md5()
                    hash.update(myFilesEncoded)
        md5 = hash.hexdigest()
        if file in files and md5 != files[file]:
            print ('File change alert: %s on %s'%(file, time.strftime("%Y-%m-%d %H:%M:%S")))
            print ('Stored hash: {} \t Current hash: {}'.format(files[file], md5))
    files.append(md5)
                # time.sleep(1)
    context = {'stored_files': stored_files, 'files': files,}
    return render(request, 'verify.html', context)

@login_required(login_url="/login/")
def output(request):
    import os, sys
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    django.setup()

    from django.utils import timezone
    from django.db import models

    from datetime import datetime
    from os import scandir
    from app.models import File

    def get_files():
        import os, hashlib
        
        for file in os.scandir('.'):
            if os.path.isfile(file):
                with open(file,'r', encoding="ascii", errors="surrogateescape") as f:
                    data =f.read
                    for chunk in iter(lambda: f.read(2048), ""):
                        myFilesEncoded = str.encode(chunk,encoding="ascii", errors="surrogateescape")
                        hash = hashlib.md5()
                        hash.update(myFilesEncoded)    
                    md5 = hash.hexdigest()
                    hashv = md5
                    info = file.stat()
                    name = file.name
                    try:
                        # creates a new instance of file and fills in the current file
                        new_file = File(
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
    context = {'files': files,}
    # return render(request, 'tables-data.html', context)
    return redirect("files")
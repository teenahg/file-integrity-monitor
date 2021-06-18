from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from app.models import File

@login_required(login_url="/login/")
def index(request):
    files = File.objects.all()
    # users = User.objects.all()
    context = {'files':files,}
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
def files(request):
    files = File.objects.all()
    context = {'files': files,}
    return render(request, 'files.html', context)

@login_required(login_url="/login/")
def output(request):
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
                        publish = published,
                        created = created_date,
                        updated = modified_date,
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
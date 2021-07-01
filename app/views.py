from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from app.models import File, cFile
import os, hashlib, sys

from django.core.mail import send_mail

from subprocess import run, PIPE

@login_required(login_url="/login/")
def index(request):
    files = File.objects.all()
    users = User.objects.all()
    context = {'files': files, 'users': users}
    return render(request, 'index.html', context)

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
    files = File.objects.all()
    hashes = []
    for file in files:
        hashes.append({'id': file.id, 'hash': hash(file)})
    context = {'files': files, 'current_hashes': hashes,}
    return render(request, 'verify.html', context)
    # prev_hashes = File.objects.all().values_list('hash_value')

@login_required(login_url="/login/")
def verification_results(request):
    stored_files = File.objects.all()
    current_files = cFile.objects.all()
    # if stored_files == current_files:
    #     print('ok')
    # else:
    #     print('not ok')
    # print(stored_files)
    # print(current_files)
    # send_mail('Subject here', 'Here is the message.', 'from@example.com', ['ozh76377@eoopy.com'], fail_silently=False,)

    import smtplib # Imports smtplib module
    import os # Imports os module
    from email.message import EmailMessage # Imports EmailMessage Class

    from bar import get_files

    for file in [item for item in os.listdir('.') if os.path.isfile(item)]:
        get_files(file)
        print(file)

    li = []
    for file in os.listdir('.'):
        if os.path.isfile(file):
            with open(file, 'r', encoding="ascii", errors="surrogateescape") as f:
                for chunk in iter(lambda: f.read(2048), ""):
                    hash = hashlib.sha256()
                    sha256 = hash.hexdigest()
                    li.append(sha256)
    for i in li:
        val = i

    #  Grabs Environment Variables
    # EMAIL_ADDRESS = 'tinashemgondwa@gmail.com'
    # PASSWORD = 'B0y5t33n@#'
    # # PASSWORD = os.environ.get('APP_PASSWORD')
    # # Creates a new message
    # msg = EmailMessage()
    # msg['Subject'] = 'Python Email'
    # msg['From'] = EMAIL_ADDRESS
    # msg['To'] = EMAIL_ADDRESS # Varies
    # msg.set_content(val)
    # # Context Manager
    # with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    #     # Logs into mail server
    #     smtp.login(EMAIL_ADDRESS, PASSWORD)
    #     smtp.send_message(msg)

    context = {'stored_files': stored_files, 'current_files': current_files}
    return render(request, 'verification_results.html', context)

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
def button(request):
    return render(request, 'res.html')

@login_required(login_url="/login/")
def all(request):
    all = File.objects.all()
    context = {'all': all}
    return render(request, "all.html", context)

@login_required(login_url="/login/")
def res(request):
    def get_files():
        import os, hashlib        
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
    return redirect("all")

@login_required(login_url="/login/")
def external(request):
    out = run([sys.executable, 'C://Users//Overwatch//Documents//file-integrity-monitor//test.py'], shell=False, stdout=PIPE)
    files = File.objects.all()
    print(out)
    return render(request, 'another.html', {'data1':out.stdout, 'files': files})

@login_required(login_url="/login/")
def continues(request):
    out = run([sys.executable, 'C://Users//Overwatch//Documents//file-integrity-monitor//continue.py'], shell=False, stdout=PIPE)
    files = File.objects.all()
    print(out)
    return render(request, 'another.html', {'data1':out.stdout, 'files': files})

@login_required(login_url="/login/")
def compare(request):
    out = run([sys.executable, 'C://Users//Overwatch//Documents//file-integrity-monitor//continue.py'], shell=False, stdout=PIPE)
    files = File.objects.all()
    print(out)
    return render(request, 'another.html', {'data1':out.stdout, 'files': files})

@login_required(login_url="/login/")
def another(request):
    my = File.objects.all()
    context = {'another': another}
    return render(render, 'another.html', context)


        # time.sleep(1)
    print(files)
    context = {'files': files}
    return render(request, "another.html", context)

@login_required(login_url="/login/")
def output(request):
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
                        hash = hashlib.sha256()
                        hash.update(myFilesEncoded)    
                        sha256 = hash.hexdigest()
                        hashv = sha256
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
    return redirect("files")

@login_required(login_url="/login/")
def checksum_verification(request):
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
    files = File.objects.all()
    context = {'files': files}
    return render(request, 'checksum_verification.html', context)

@login_required(login_url="/login/")
def verify(request):
    import os,hashlib,time
    files = File.objects.all()
    hashes = File.objects.all().values_list('hash_value')
    hashes_list = list(hashes)
    current_sha256 = []
    for file in os.listdir('.'):
        if os.path.isfile(file):
            with open(file,'r', encoding="ascii", errors="surrogateescape") as f:
                data = f.read
                for chunk in iter(lambda: f.read(2048), ""):
                    myFilesEncoded = str.encode(chunk,encoding="ascii", errors="surrogateescape")
                    hash = hashlib.sha256()
                    hash.update(myFilesEncoded)
                    sha256 = hash.hexdigest()
                    current_sha256.append(sha256)
    context = {'files': files, 'current_sha256': current_sha256, 'hashes_list': hashes_list}
    return render(request, 'verify.html', context)

        # for i in current_sha256:
            # print(i)
                # for file in stored_files_list:
                #     if file != sha256:
                # files.append(sha256)
                # if file in stored_files and sha256 != stored_files[file]:
                    # print(file)
                    # print ('File change alert: %s on %s'%(file, time.strftime("%Y-%m-%d %H:%M:%S")))
                    # print ('Stored hash: {} \t Current hash: {}'.format(files[file], sha256))
    # print(files)
                # time.sleep(1)
    # context = {'stored_files': stored_files, 'files': files,}
    # context = {'files': files,}
    # return render(request, 'verify.html', context)

    # import hashlib
    # hash = hashlib.sha256()
    # res = hash.hexdigest()
    # print(res)
    # return res
    # import secrets
    # res = secrets.token_hex(16)
    # print(res)
    # return res
    # import os,hashlib,time
    # files={}
    # for file in [item for item in os.listdir('.') if os.path.isfile(item)]:
    #     with open(file,'r', encoding="ascii", errors="surrogateescape") as f:
    #         hash = hashlib.sha256()
    #         for chunk in iter(lambda: f.read(2048), ""):
    #             myFilesEncoded = str.encode(chunk,encoding="ascii", errors="surrogateescape")
    #             hash.update(myFilesEncoded)
    #     sha256 = hash.hexdigest()
    #     if file in files and sha256 != files[file]:
    #         print ('File change alert: %s on %s'%(file, time.strftime("%Y-%m-%d %H:%M:%S")))
    #         print ('Stored hash: {} \t Current hash: {}'.format(files[file], sha256))
    #         files[file]=sha256
    # print(sha256)
    # return sha256

    # import os, hashlib
    # hashes_list = {}
    # for file in [item for item in os.listdir('.') if os.path.isfile(item)]:
    #     with open(file,'r', encoding="ascii", errors="surrogateescape") as f:
    #         data =f.read
    #         hash = hashlib.sha256()
    #         for chunk in iter(lambda: f.read(2048), ""):
    #             myFilesEncoded = str.encode(chunk, encoding="ascii", errors="surrogateescape")
    #             hash.update(myFilesEncoded)
    #     sha256 = hash.hexdigest()
    # hashes_list.append(sha256)
    # print(hashes_list)
    # return hashes_list
    
        # if os.path.isfile(file):
            # with open(file,'r', encoding="ascii", errors="surrogateescape") as f:
    #             data =f.read
    #             for chunk in iter(lambda: f.read(2048), ""):
    #                 myFilesEncoded = str.encode(chunk,encoding="ascii", errors="surrogateescape")
    #                 hash = hashlib.sha256()
    #                 hash.update(myFilesEncoded)
    # sha256 = hash.hexdigest()
    # print(sha256)
    # return sha256

    # def hash():
#     def get_files():
#         for file in os.scandir('.'):
#             if os.path.isfile(file):
#                 with open(file,'r', encoding="ascii", errors="surrogateescape") as f:
#                     data =f.read
#                     for chunk in iter(lambda: f.read(2048), ""):
#                         myFilesEncoded = str.encode(chunk,encoding="ascii", errors="surrogateescape")
#                         hash = hashlib.sha256()
#                         hash.update(myFilesEncoded)    
#                         sha256 = hash.hexdigest()
#                         hashv = sha256
#                     info = file.stat()
#                     name = file.name
#                     try:
#                         # creates a new instance of file and fills in the current file
#                         new_file = cFile(
#                             name = name, # file name
#                             location = file.path, # file path
#                             hash_value = hashv, # file's created hash value
#                             )
#                         new_file.save()
#                     except Exception as e:
#                         print(e, e.__traceback__, " at line ", e.__traceback__.tb_lineno)
#                     finally:
#                         print("All files have been saved")
#     get_files()
#     context = {'files': files,}
#     # return render(request, 'tables-data.html', context)
#     return redirect("verify")
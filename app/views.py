from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from app.models import File, cFile
import os, hashlib

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
    if stored_files == current_files:
        print('ok')
    else:
        print('not ok')
    # print(stored_files)
    # print(current_files)
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

def hash():
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
    context = {'files': files,}
    # return render(request, 'tables-data.html', context)
    return redirect("verify")

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
    # return render(request, 'tables-data.html', context)
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
    files = File.objects.all()
    context = {'files': files}
    return render(request, 'checksum_verification.html', context)

@login_required(login_url="/login/")
def verify(request):
    import os,hashlib,time
    files = File.objects.all()
    hashes = File.objects.all().values_list('hash_value')
    hashes_list = list(hashes)
    # print(stored_files_list)
    # while True: # Continuously monitors, not recommended for web because the page won't stop loading
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
                    print(current_sha256, sha256)
    return render(request, 'verify.html')
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
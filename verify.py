import os,hashlib,time
    stored_files = File.objects.all()
    files={}
    # while True:
    for file in [item for item in os.listdir('.') if os.path.isfile(item)]:
        with open(file,'r', encoding="ascii", errors="surrogateescape") as f:
            hash = hashlib.md5()
            for chunk in iter(lambda: f.read(2048), ""):
                myFilesEncoded = str.encode(chunk,encoding="ascii", errors="surrogateescape")
                hash.update(myFilesEncoded)
            md5 = hash.hexdigest()
            if file in files and md5 != files[file]:
                print ('File changed: %s on %s'%(file, time.strftime("%Y-%m-%d %H:%M:%S")))
                print ('Stored hash: {} \t Recent hash: {}'.format(files[file], md5))
                files[file]=md5
        # time.sleep(1)
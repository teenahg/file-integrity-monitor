import os,hashlib,time
hash = hashlib.sha256()
files={}
# while True:
for file in [item for item in os.listdir('.') if os.path.isfile(item)]:
    with open(file,'r', encoding="ascii", errors="surrogateescape") as f:
        for chunk in iter(lambda: f.read(2048), ""):
            myFilesEncoded = str.encode(chunk,encoding="ascii", errors="surrogateescape")
            hash.update(myFilesEncoded)
        sha256 = hash.hexdigest()
        if file in files and sha256 == files[file]:
            print("all is well")
        elif file in files and sha256 != files[file]:
            print ('File change alert: %s on %s'%(file, time.strftime("%Y-%m-%d %H:%M:%S")))
            print ('Stored hash: {} \t Current hash: {}'.format(files[file], sha256))
            files[file]=sha256
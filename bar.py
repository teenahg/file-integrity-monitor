def get_files(file):
    import os,hashlib,time

    for file in [item for item in os.listdir('.') if os.path.isfile(item)]:
        with open(file,'r', encoding="ascii", errors="surrogateescape") as f:
            hash = hashlib.sha256()
            for chunk in iter(lambda: f.read(2048), ""):
                myFilesEncoded = str.encode(chunk,encoding="ascii", errors="surrogateescape")
                hash.update(myFilesEncoded)
                sha256 = hash.hexdigest()
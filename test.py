import os, hashlib 
hash = hashlib.sha256()  
li = {}     
for file in os.listdir('.'):
    if os.path.isfile(file):
        with open(file,'r', encoding="ascii", errors="surrogateescape") as f:
            data =f.read
            for chunk in iter(lambda: data(2048), ""):
                myFilesEncoded = str.encode(chunk,encoding="ascii", errors="surrogateescape")
                hash.update(myFilesEncoded)    
        sha256 = hash.hexdigest()
        li.update(file = file, hash = sha256)
        print(li)
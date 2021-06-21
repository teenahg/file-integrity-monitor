import os,hashlib
# Script content
for file in [item for item in os.listdir('.') if os.path.isfile(item)]:
  with open(file,'r', encoding="ascii", errors="surrogateescape") as f:
    data =f.read
    hash = hashlib.md5()
    for chunk in iter(lambda: f.read(2048), ""):
      myFilesEncoded = str.encode(chunk,encoding="ascii", errors="surrogateescape")
      hash.update(myFilesEncoded)

      md5 = hash.hexdigest()
      print(file, md5)
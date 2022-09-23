import zipfile
import os

class unzip_Files:
    def unzip_file(filename):
        z=zipfile.ZipFile(filename)
        path=os.path.dirname(filename)
        z.extractall(path=path)

unzip_Files.unzip_file(filename= "F:\Data\Documents")

'''
The single responsibility principle comes from Robert C Martin, more commonly known as Uncle Bob Martin.
It statates:

###
A class should have only one reason to change.
###

This means that a class should have only one responsibility as expressed throuhg its methods. If a class takes care of more 
than one task, then you should separate those tasks into dedicated classes with descriptive names


'''

# Example of a class violating Single Responsibility principle

from pathlib import Path 
from zipfile import ZipFile 


class FilaManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding='utf-8'):
        return self.path.read_text(encoding)

    def write(self, data, encoding='utf-8'):
        self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archieve:
            archieve.extractall()

"""
In this example FileManager class has two different responsibilites. It manages files using read, write methods.
It also deals with zip archives by providing compress decompress methods
"""


# how it should look like instead

from pathlib import Path 
from zipfile import ZipFile 


class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, encoding="utf-8"):
        self.path.write_text(encoding)


class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode='r') as archive:
            archive.extractall()
            
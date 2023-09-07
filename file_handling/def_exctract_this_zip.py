"""The extract_this() function takes one or
more arguments in the following order:

zip_name - the name of the zip archive, for example, data.zip
*args - variable number of positional arguments,

each of which is the name of some file
The function extracts the *args files from the zip_name archive
to the program folder. If no file name is passed to the function
for extraction, then the function extracts all files from the archive."""

from zipfile import ZipFile


def extract_this(zip_name, *args):
    with ZipFile(zip_name) as file:
        if len(args) > 0:
            for i in args:
                file.extract(i)
        else:
            file.extractall()

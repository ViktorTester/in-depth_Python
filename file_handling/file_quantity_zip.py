"""There is a workbook.zip archive containing various folders and files.
The program displays a single number — the number of files in this archive.

The folder is not considered a file."""

from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.namelist()

    counter = 0

    for i in info:
        if '.' in i:
            counter += 1

    print(counter)

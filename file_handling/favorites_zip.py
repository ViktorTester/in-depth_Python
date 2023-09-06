"""There is a workbook.zip archive containing various folders and files.
The program displays the names of files from this archive that were created
or modified after 2021-11-30 14:22:00. The file names are
in lexicographic order, each on a separate line."""

from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()

    needed_time = datetime(2021, 11, 30, 14, 22, 00)

    arr = []

    for j in info:
        file_name = j.filename.split('/')[-1]
        i = datetime(*j.date_time)
        if i > needed_time and file_name != '':
            arr.append(file_name)

    for x in sorted(arr):
        print(x)

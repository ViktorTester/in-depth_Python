"""There is a workbook.zip archive containing various folders and files.
Write a program that displays the names of all files from this archive
in lexicographic order, indicating for each its date of modification,
as well as the volume before and after compression."""

from zipfile import ZipFile
from datetime import datetime

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()

    d = {}

    for j in info:
        file_name = j.filename.split('/')[-1]
        if file_name != '':
            d[file_name] = j

    for key, value in sorted(d.items()):
        print(key)
        print(f'  File modification date: {datetime(*value.date_time)}')
        print(f'  Source file size: {value.file_size} byte(s)')
        print(f'  Size of the compressed file: {value.compress_size} byte(s)')
        print()

"""There is a workbook.zip archive containing various folders and files.
The program displays the name of the file from this archive,
which has the best compression ratio."""

from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()

    d = {}

    for j in info:
        if j.file_size != 0:
            d[j] = j.file_size / j.compress_size * 100

    max_compress = 0
    file_name = ''

    for key, value in d.items():
        if value > max_compress:
            max_compress = value
            file_name = key.filename.split('/')[-1]

    print(file_name)

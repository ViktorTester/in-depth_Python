"""There is a workbook.zip archive containing various folders and files.
The program displays the total size of files in this archive
in compressed and uncompressed forms in bytes."""

from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    info = zip_file.infolist()

    file_size = 0
    compressed_size = 0

    for i in info:
        file_size += i.file_size
        compressed_size += i.compress_size

print(f'Amount of source files: {file_size} bytes(s)')
print(f'Compressed files: {compressed_size} bytes(s)')

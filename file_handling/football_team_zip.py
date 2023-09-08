"""There is a data.zip archive containing various folders and files.
Among them there are several JSON files, each of which
contains information about a football player

The program processes only these JSON files and displays the names and
surnames of football players playing for the Arsenal football club.
The players are arranged in the lexicographic order of their first
names, and if there is a match, in the lexicographic order
of their surnames, each on a separate line."""

from zipfile import ZipFile

with ZipFile('/Users/aggro/Desktop/data.zip') as zip_file:
    info = zip_file.namelist()
    arr = []

    for i in info:
        if 'player' in i:
            with zip_file.open(i) as file:
                arr.append(file.read().decode('utf-8').split())

    for j in sorted(arr, key=lambda key: (key[2], key[3])):
        for x in j:
            if x[:-1] == '"Arsenal"':
                print(j[2][1:-2] + ' ' + j[4][1:-2])

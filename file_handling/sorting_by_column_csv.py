"""There is a deniro.csv file, each column of
which contains either only numbers or only words:

The program sorts the contents of the given file
by the specified column. The data is sorted in
ascending numerical order if the column contains
numbers, and in lexicographic word order
if the column contains words."""

import csv

with open('deniro.csv', encoding='utf-8') as file:
    ind = int(input()) - 1
    arr = []
    rows = csv.reader(file)

    for x in rows:
        for i, y in enumerate(x):
            if y.isdigit():
                x[i] = int(y)
        arr.append(x)

    for v in sorted(arr, key=lambda b: b[ind]):
        print(f'{v[0]},{v[1]},{v[2]}')

"""The csv_columns() function takes one argument:

filename - the name of the csv file, for example, data.csv

The function returns a dictionary in which the key is the filename
column name and the value is a list of the elements of this column."""

import csv


def csv_columns(filename: csv) -> dict:
    with open(filename, encoding='utf-8') as file:
        rows = csv.DictReader(file, delimiter=',')
        d = {}
        for row in rows:
            for key, value in row.items():
                if key not in d:
                    d[key] = [value]
                else:
                    d[key].append(value)

        return d

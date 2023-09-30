"""You have sales data for the year, divided into four quarterly files:
'quarter1.csv', 'quarter2.csv', 'quarter3.csv', and 'quarter4.csv'.
In each file, the first column indicates the name of the product,
and the subsequent columns indicate the quantity of
product sold in kilograms for a particular month.

There is also a 'prices.json' file containing a dictionary in which
the key is the product name and the value is the price per kilogram.

The program displays a single number - the amount earned during the year."""

from collections import defaultdict

import csv, json

with (open('quarter1.csv', encoding='utf-8') as file1,
      open('quarter2.csv', encoding='utf-8') as file2,
      open('quarter3.csv', encoding='utf-8') as file3,
      open('quarter4.csv', encoding='utf-8') as file4,
      open('prices.json', encoding='utf-8') as prices):
    rows1 = list(csv.reader(file1))
    rows2 = list(csv.reader(file2))
    rows3 = list(csv.reader(file3))
    rows4 = list(csv.reader(file4))
    data = json.load(prices)

    total = rows1[1:] + rows2[1:] + rows3[1:] + rows4[1:]
    arr = [(row[0], int(row[1]) + int(row[2]) + int(row[3])) for row in total]

    ddict = defaultdict(int)

    for i, j in arr:
        ddict[i] += j

    earned = 0

    for key1, value1 in ddict.items():
        for key2, value2 in data.items():
            if key1 == key2:
                earned += value1 * value2

    print(earned)

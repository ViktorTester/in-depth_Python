"""There is a 'food_services.json' file containing a list of
JSON objects that represent food service data.

The program determines all types of establishments and for each
type finds the largest establishment of this type
(has the largest number of seats). The program displays all types
of establishments in lexicographic order, indicating
for each the largest establishment and the number of seats in it."""

import json

with open('food_services.json', encoding='utf-8') as file1:
    rows = json.load(file1)

    d = {}

    for row in rows:
        if row['TypeObject'] not in d:
            d[row['TypeObject']] = [row['Name'], row['SeatsCount']]
        else:
            if row['SeatsCount'] > d[row['TypeObject']][1]:
                d[row['TypeObject']] = [row['Name'], row['SeatsCount']]

    for key, value in sorted(d.items()):
        print(f'{key}: {value[0]}, {value[1]}')

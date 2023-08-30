"""There is a food_services.json file containing a list of
JSON objects that represent food service data.

The program determines the district with the most establishments
and displays the name of this district and the number of establishments
in it, and also determines the chain with the largest number of
establishments and displays the name of this chain
and the number of establishments of this chain."""

import json

with open('food_services.json', encoding='utf-8') as file1:
    rows = json.load(file1)

    d, d2 = {}, {}

    for row in rows:
        if row['District'] not in d:
            d[row['District']] = 1
        else:
            d[row['District']] += 1

        if row['IsNetObject'] == 'yes':
            if row['OperatingCompany'] not in d2:
                d2[row['OperatingCompany']] = 1
            else:
                d2[row['OperatingCompany']] += 1

    for key, value in d.items():
        if value == max(d.values()):
            print(f'{key}: {value}')

    for key1, value1 in d2.items():
        if value1 == max(d2.values()):
            print(f'{key1}: {value1}')

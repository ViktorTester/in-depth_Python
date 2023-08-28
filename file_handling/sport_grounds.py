"""There is a playgrounds.csv file with information about sports
grounds in some city. The first column contains the site type,
the second - the administrative district, the
third - the name of the district, the fourth - the address.

The program creates a JSON object, the key in which is the
administrative district, and the value is a JSON object,
in which, in turn, the key is the name of the district
related to this administrative district, and the value
is a list of addresses of all sites in this district."""

import json
import csv

with open('playgrounds.csv', encoding='utf-8') as file1:
    data = list(csv.DictReader(file1, delimiter=';', quotechar='"'))

    d = {}

    for row in data:
        adm_area = row['AdmArea']
        district = row['District']
        address = row['Address']

        if adm_area in d:
            if district in d[adm_area]:
                d[adm_area][district].append(address)
            else:
                d[adm_area][district] = [address]
        else:
            d[adm_area] = {district: [address]}

with open('addresses.json', 'w', encoding='utf-8') as end:
    json.dump(d, end, ensure_ascii=False, indent=4)

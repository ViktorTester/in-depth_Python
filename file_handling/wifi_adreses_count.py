"""There is a wifi.csv file that contains data about the city's Wi-Fi.
The first column contains the name of the county, the second - the name
of the district, the third - the address, the fourth - the
number of access points at this address.

The program determines the number of access points in each area and
displays the names of all areas, for each indicating the
corresponding number of access points, each on a separate line.

The names of the districts are arranged in descending order of
the number of access points, if the number of access points
is the same - in lexicographic order."""

import csv

with open('wifi.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')

    d = {}

    for row in rows:
        district_val = int(row['number_of_access_points'])
        if row['district'] not in d:
            d[row['district']] = district_val
        else:
            d[row['district']] = d.get(row['district'], 0) + district_val

    for key, value in sorted(d.items(), key=lambda x: (-x[1], x[0])):
        print(f'{key}: {value}')

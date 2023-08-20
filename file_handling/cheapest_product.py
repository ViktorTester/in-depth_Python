"""The program determines the cheapest product, as well as the store
where it is sold. There is a prices.csv file that contains information
about the prices of products in various stores. The first column
contains the name of the store, and the subsequent columns contain
the price of the corresponding product in that store."""

import csv

with open('prices.csv', mode='r', encoding='utf-8') as file:
    rows = list(csv.DictReader(file, delimiter=';'))
    max_price = 999
    cheapest = ''
    cheapest_shop = ''
    for row in rows:
        for key, value in row.items():
            if value.isdigit():
                if int(value) < max_price:
                    max_price = int(value)
                    cheapest = key
        for key, value in row.items():
            if key == cheapest and value == str(max_price):
                cheapest_shop = row['Shop']

    print(f'{cheapest}: {cheapest_shop}')

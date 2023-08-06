"""There is a sales.csv file that contains pricing data for
various household appliances. The first column contains the
product name, the second column contains the old price, and
the third column contains the new discounted price.

The program displays the names of those goods, the price of
which has decreased. Items are listed in their
original order, each on a separate line."""

import csv

with open('sales.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')
    for row in rows:
        if int(row['new_price']) < int(row['old_price']):
            print(row['name'])

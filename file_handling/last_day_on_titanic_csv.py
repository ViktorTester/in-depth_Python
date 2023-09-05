"""There is a titanic.csv file that contains data about the passengers
who were present on board the Titanic. The first column contains one
if the passenger survived and zero otherwise, the second column contains
the passenger's full name, the third column contains gender,
and the fourth column indicates age.

The program displays the names of surviving passengers who were under
18 years old, each on a separate line. Moreover, the names of all male
passengers are located first, and then the female ones, while the names
directly in the male and female lists are located in their original order.
"""

import csv

with open('titanic.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')

    arr = []
    women = []

    for row in rows:
        if float(row['age']) < 18 and row['survived'] == '1':
            arr.append(row["name"].split('.'))

    for i in arr:
        if i[0] in ['Master', 'Mr']:
            print('.'.join(i))
        else:
            women.append(i)

    for j in women:
        print('.'.join(j))

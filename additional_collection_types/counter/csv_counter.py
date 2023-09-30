"""There is a file 'name_log.csv', which contains logs of user name changes.
The first column records the changed username, the second column the email address,
and the third column the date and time of the change.
In this case, the user cannot change the email, only the name.

The program determines how many times the user has changed his name.
The program should display the email addresses of users, indicating for
each the corresponding number of changed names."""

from collections import Counter
import csv

with open('name_log.csv', encoding='utf-8') as file:
    rows = list(csv.reader(file))

    arr = [row[1] for row in rows[1:]]

    for key, value in sorted(Counter(arr).items()):
        print(f'{key}: {value}')

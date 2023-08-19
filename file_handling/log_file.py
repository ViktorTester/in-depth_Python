"""There is a name_log.csv file, which contains the username change
logs. The first column shows the username that was changed,
the second column shows the email address, and the third column
shows the date and time the change was made. At the same time,
the user cannot change the email, only the name.

The program selects only the most recent entries for each user from
the name_log.csv file and writes them to the new_name_log.csv file.
In the new_name_log.csv file, the first line is the column headings,
the same as in the name_log.csv file. The logs in the final file are
arranged in the lexicographic order of the names of the user's e-mail boxes."""

import csv
from datetime import datetime

with open('name_log.csv', encoding='utf-8') as file:
    rows = list(csv.reader(file))

    d = {}
    arr = []

    for i in rows[1:]:
        i[2] = datetime.strptime(i[2], '%d/%m/%Y %H:%M')

    for row in sorted(rows[1:], key=lambda x: x[2]):
        d[row[1]] = [row[0], row[1], row[2]]

    columns = rows[0]

    for key, value in sorted(d.items(), key=lambda x: x[0]):
        arr.append({'username': value[0], 'email': key, 'dtime': value[2].strftime('%d/%m/%Y %H:%M')})

with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=columns, delimiter=',')
    writer.writeheader()
    writer.writerows(arr)

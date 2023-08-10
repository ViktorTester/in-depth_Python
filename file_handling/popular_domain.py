"""There is a data.csv file that contains non-recurring data about
users of some resource. The first column contains the user's first
name, the second column contains the last name,
and the third column contains the email address.

The program creates a domain_usage.csv file with the following content:

domain,count
rambler.ru,24
iCloud.com,29
...

where the first column contains the name of the mail domain, and the
second column contains the number of users using this domain.
Domains in the file are arranged in ascending order of the number
of their uses, if the number of uses is the same, in lexicographic order."""

import csv

with open('data.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=',')

    d = {}

    for row in rows:
        mail = row['email'].split('@')
        if mail[1] not in d:
            d[mail[1]] = 1
        else:
            d[mail[1]] = d.get(mail[1], 0) + 1

    data = []

    for key, value in sorted(d.items(), key=lambda x: (x[1], x[0])):
        data.append({'domain': key, 'count': value})

    columns = ['domain', 'count']

with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=columns, delimiter=',')
    writer.writeheader()
    writer.writerows(data)
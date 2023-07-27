"""A list of employees of the organization is given, in which
their last names, first names and dates of birth are indicated.

The program detects the youngest employee celebrating his
birthday within the next seven days and displays his first
and last name, separated by a space. If there are
no such employees, the program displays the text:

'Birthdays are not planned'"""

from datetime import datetime, timedelta

d = {}

v = input().split('.')
cur = datetime(int(v[2]), int(v[1]), int(v[0])) + timedelta(days=1)

for i in range(int(input())):
    s = input()
    my_date = datetime(int(s[-4:]), int(s[-7:-5]), int(s[-10:-8]))
    if my_date not in d:
        d[my_date] = [s[:-11]]
    else:
        d[my_date].append(s[:-11])

arr = []
end_date = cur + timedelta(days=7)

while cur != end_date:
    for key, value in d.items():
        if cur.month == key.month and cur.day == key.day:
            arr.append([key, value])
    cur += timedelta(days=1)

max_date = datetime(1, 1, 1)
name = ''

if len(arr) > 0:
    for x in arr:
        if x[0] > max_date:
            max_date = x[0]
            name = x[1]
    print(*name)
else:
    print('Birthdays are not planned')
"""A list of employees of the organization is given, in which
their last names, first names and dates of birth are indicated.

The program displays the date on which the largest number of
employees celebrate their birthday, in the format DD.MM.YYYY.
If there are several such dates, the program displays them all
in ascending order, each on a separate line, in the same format."""

from datetime import datetime

d = {}
for i in range(int(input())):
    s = input()
    my_date = datetime(int(s[-4:]), int(s[-7:-5]), int(s[-10:-8]))
    if my_date not in d:
        d[my_date] = [s[:-11]]
    else:
        d[my_date].append(s[:-11])

arr = []
max_len = 1

for key, value in sorted(d.items()):
    if len(value) > max_len:
        max_len = len(value)
        arr.append(key)

for key, value in sorted(d.items()):
    if len(value) == max_len and key not in arr:
        arr.append(key)

for j in arr:
    print(j.strftime('%d.%m.%Y'))

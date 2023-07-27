"""A list of employees of the organization is given, in which their
last names, first names and dates of birth are indicated.
The program determines the oldest employee and displays his date
of birth, first name and last name, separated by a space.
If there are several such employees, the program displays
their date of birth, as well as their number, separated by a space."""

from datetime import datetime

d = {}
for i in range(int(input())):
    s = input()
    my_date = datetime(int(s[-4:]), int(s[-7:-5]), int(s[-10:-8]))
    if my_date not in d:
        d[my_date] = [s[:-11]]
    else:
        d[my_date].append(s[:-11])

for key, value in sorted(d.items()):
    if len(value) > 1:
        print(key.strftime('%d.%m.%Y'), len(value))
    else:
        print(key.strftime('%d.%m.%Y'), *value)
    break

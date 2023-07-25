"""Proof that the 13th of the month most often falls on a Friday.
The program calculates how many thirteenth numbers fall
on each day of the week from 01/01/0001 to 12/31/9999."""

from datetime import datetime, timedelta

start = '01.01.0001'.split('.')
end = '31.12.9999'.split('.')

start_date = datetime(int(start[2]), int(start[1]), int(start[0]))
end_date = datetime(int(end[2]), int(end[1]), int(end[0]))

d = {}

while start_date != end_date:
    if start_date.day == 13:
        weekend = start_date.isoweekday()
        if weekend not in d:
            d[weekend] = 1
        else:
            d[weekend] += 1

    start_date += timedelta(days=1)

for key, value in sorted(d.items()):
    print(value)

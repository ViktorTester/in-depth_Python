"""There is a file meetings.csv, where the date and time of the meeting are
indicated, in which the first column contains the last name,
the second - the first name, the third - the date in the DD.MM.YYYY format,
and the fourth - the time in the HH:MM format:

The program displays the names and surnames of people with whom a meeting
is scheduled, having previously sorted them by date and time of the meeting
from earliest to latest. Last names and first names
are each located on a separate line."""

from collections import namedtuple
import csv
from datetime import datetime

with open('meetings.csv', encoding='utf-8') as file:
    rows = list(csv.reader(file))

    Friends = namedtuple('Friends', ['surname', 'name', 'meeting_date', 'meeting_time'])

    arr = []

    for i in rows[1:]:
        my_date = datetime.strptime(i[2], '%d.%m.%Y')
        my_time = datetime.strptime(i[3], '%H:%M')
        friends = Friends(i[0], i[1], my_date, my_time)
        arr.append(friends)

    sorted_friends = sorted(arr, key=lambda z: (z.meeting_date, z.meeting_time))

    for j in sorted_friends:
        print(j.surname, j.name)

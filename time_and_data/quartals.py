"""The 'dates' list contains dates. The code below is to
make it output the year and quarter number of each date
from the given list. The date components are in source
order, each on a separate line, in the following format:

<year>-Q<quarter number>"""

from datetime import date

dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27),
         date(2021, 10, 11), date(2020, 3, 13), date(2000, 7, 7), date(1999, 4, 14),
         date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]

d = {1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9], 4: [10, 11, 12]}

for i in dates:
    for key, value in d.items():
        if i.month in value:
            print(f'{i.year}-Q{key}')
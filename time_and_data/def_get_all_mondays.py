"""The get_all_mondays() function takes one argument:

'year' - natural number

The function returns an ascending sorted list of all
dates (date type) of the year 'year' that fall on a Monday."""

import calendar
from datetime import date, timedelta


def get_all_mondays(year: int) -> list:
    arr = []
    my_date = date(year, 1, 1)

    while my_date != date(year + 1, 1, 1):
        if calendar.weekday(my_date.year, my_date.month, my_date.day) == 0:
            arr.append(my_date)
        my_date += timedelta(days=1)

    return arr


print(get_all_mondays(2021))

"""The get_days_in_month() function takes two
arguments in the following order:

'year' is a natural number
'month' - the full name of the month in English

The function returns an ascending sorted list of all
dates (date type) of month 'month' and year 'year'."""

import calendar
from datetime import date, timedelta


def get_days_in_month(year: int, month: str) -> list:
    arr = []
    months = list(calendar.month_name)
    days = calendar.monthrange(int(year), months.index(month))
    my_date = date(year, months.index(month), 1)

    for _ in range(days[1]):
        arr.append(my_date)
        my_date += timedelta(days=1)

    return arr


print(get_days_in_month(2021, 'December'))

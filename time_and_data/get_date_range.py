"""The get_date_range() function returns a list of dates
(date type) from start to end inclusive. If start > end,
the function returns an empty list."""

from datetime import date


def get_date_range(start: date, end: date) -> list:
    start = start.toordinal()
    end = end.toordinal()

    arr = [date.fromordinal(start + i) for i in range(end - start + 1)]

    return arr


date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')

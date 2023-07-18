"""The function prints lucky dates in ascending order,
each on a separate line, in the format month_name DD, YYYY.

A lucky date is one in which the year is 1992 and
the sum of the digits of the month number and
the day of the month number is 29."""

from datetime import date


def print_good_dates(dates: list):
    arr = [i for i in dates if i.year == 1992 and i.day + i.month == 29]

    for j in sorted(arr):
        print(j.strftime('%B %d, %Y'))


dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20), date(1992, 8, 20)]
print_good_dates(dates)

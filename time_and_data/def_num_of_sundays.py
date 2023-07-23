"""The function returns the number ofSundays in the 'year' year."""

from datetime import timedelta, date


def num_of_sundays(year: int) -> int:
    counter = 0
    my_date = date(year, 1, 1)
    while my_date.year == year:
        if my_date.isoweekday() == 7:
            counter += 1
        my_date += timedelta(days=1)

    return counter

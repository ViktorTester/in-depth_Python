"""The function returns the number of saturdays
between the dates start and end inclusive."""

from datetime import date


def saturdays_between_two_dates(start: date, end: date) -> int:
    values = [start, end]
    start = max(values).toordinal()
    end = min(values).toordinal()
    counter = 0

    if date.fromordinal(end).isoweekday() == date.fromordinal(end).isoweekday() == 6:
        return 1
    if start == end:
        return 0
    while end != start:
        end += 1
        if date.fromordinal(end).isoweekday() == 6:
            counter += 1

    return counter

"""The dates() generator function takes two arguments in the following order:

start — date, date type
count - natural number, default value is None

If 'count' is None, the function returns a generator that generates a sequence
of the maximum number of dates allowed (type date), starting with the 'start' date.

If 'count' has a natural number as its value, the function returns a generator
that generates a sequence of 'count' dates (of type date), starting with the
'start' date, and then raises a StopIteration exception."""

from datetime import date, timedelta


def dates(start, count=None):
    current_date = start
    generated_count = 0

    while count is None or generated_count < count:
        yield current_date
        generated_count += 1

        try:
            current_date += timedelta(days=1)
        except OverflowError:
            break


generator = dates(date(2022, 3, 8), 5)

print(*generator)

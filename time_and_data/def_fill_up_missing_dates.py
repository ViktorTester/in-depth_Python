"""The function returns a list containing all the
dates in the dates list, in ascending order,
plus any missing intermediate dates."""

from datetime import date, timedelta


def fill_up_missing_dates(dates: list) -> list:
    my_set = set()
    result = []
    for i in dates:
        day, month, year = i.split('.')
        my_date = date(int(year), int(month), int(day))
        my_set.add(my_date)

    arr = sorted(my_set)
    delta = arr[-1] - arr[0]
    counter = 0

    for _ in range(delta.days + 1):
        result.append((arr[0] + timedelta(days=counter)).strftime('%d.%m.%Y'))
        counter += 1

    return result

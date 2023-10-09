"""The get_weekday() function takes one argument:

number — integer (from 1 to 7 inclusive)

The function returns the full name of the day of the week, which corresponds to number, and:

if number is not an integer, the function raises an exception:
TypeError('Argument is not an integer')

if number is an integer but does not belong to the range [1;7],
the function raises an exception:
ValueError('The argument does not belong to the required range')"""

from calendar import day_name

d = {}
counter = 0

for i in day_name:
    counter += 1
    d[i] = counter


def get_weekday(number: int) -> str:
    if not isinstance(number, int):
        raise TypeError('Argument is not an integer')
    if int(number) < 1 or int(number) > 7:
        raise ValueError('Argument is not in the required range')
    for key, value in d.items():
        if number == value:
            return key

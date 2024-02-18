"""The drop_while_negative() function takes one argument:

iterable — an iterable object whose elements are integers

The function returns an iterator that generates all the numbers
of the iterable object, starting with the first non-negative number."""

from itertools import dropwhile


def drop_while_negative(iterable):
    return dropwhile(lambda num: num < 0, iterable)


numbers = [-3, -2, -1, 0, 1, 2, 3]

print(*drop_while_negative(numbers))

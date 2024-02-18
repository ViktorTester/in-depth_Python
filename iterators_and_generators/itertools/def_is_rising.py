"""The is_rising() function takes one argument:

iterable - an iterable object whose elements are numbers

The function returns True if the elements of the iterable object
are arranged in strictly ascending order, or False otherwise."""

from itertools import pairwise


def is_rising(iterable):
    for x, y in pairwise(iterable):
        if x + 1 == y:
            continue
        return False
    return True


iterator = iter([1, 1, 1, 2, 3, 4])

print(is_rising(iterator))

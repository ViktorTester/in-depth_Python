"""The sum_of_digits() function takes one argument:

iterable - an iterable object whose elements are natural numbers

The function returns a single number - the sum of the digits of
all numbers present in the iterable 'iterable' object."""

from itertools import chain


def sum_of_digits(iterable):
    s = ''.join(map(str, iterable))

    return sum(map(int, chain(s)))


print(sum_of_digits((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

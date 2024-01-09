"""The factorials() function accepts one argument:

n — natural number

The function returns an iterator that generates a sequence of 'n' numbers,
each of which is a factorial of the next natural number."""

from itertools import accumulate


def factorials(n):
    return accumulate(range(1, n + 1), lambda x, y: x * y)

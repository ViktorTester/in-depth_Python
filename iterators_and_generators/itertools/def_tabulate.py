"""The tabulate() function takes one argument:

func — arbitrary function

The function tabulate() returns an iterator that generates an infinite
sequence of values returned by the 'func' function
first with argument 1, then 2, then 3, and so on."""

from itertools import count


def tabulate(func):
    return map(func, count(1))

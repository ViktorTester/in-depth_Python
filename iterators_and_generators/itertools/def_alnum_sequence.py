"""The function alnum_sequence() does not accept any arguments.

The function returns an iterator that cyclically generates an
infinite sequence of natural numbers and uppercase Latin letters:
1, A, 2, B, 3, C, .., X, 25, Y, 26, Z"""

from string import ascii_uppercase as letters
from itertools import cycle, count


def alnum_sequence():
    generator = (i for j in zip(count(1), letters) for i in j)
    yield from cycle(generator)


alnum = alnum_sequence()

print(*(next(alnum) for _ in range(55)))

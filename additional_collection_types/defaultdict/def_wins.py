"""Every summer the school hosts chess competitions, during which statistics
of victories and defeats are kept. Each game is described by a tuple of two
elements, where the first element is the name of the winning student,
the second element is the name of the losing student.

The wins() function takes one argument:

pairs is an iterable object whose elements are tuples,
each of which represents a pair of winner-loser names

The function returns a dictionary in which the key is the name of the student,
and the value is a set (type set) of the names of the students he defeated."""

from collections import defaultdict


def wins(pairs: list) -> dict:
    ddict = defaultdict(set)
    for i, j in pairs:
        ddict[i].add(j)

    for key, value in ddict.items():
        ddict[key] = value

    return ddict
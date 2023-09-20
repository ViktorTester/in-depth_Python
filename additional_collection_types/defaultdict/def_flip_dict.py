"""The flip_dict() function takes one argument:

dict_of_lists is a dictionary in which the key is a number or
string and the value is a list of numbers or strings.

The function returns a new dictionary (of type defaultdict with type list
as the default value), which is an inverted dictionary of dict_of_lists."""

from collections import defaultdict


def flip_dict(dict_of_lists: dict) -> dict:
    ddict = defaultdict(list)

    for key, value in dict_of_lists.items():
        for x in value:
            ddict[x].append(key)

    for key1, value1 in ddict.items():
        ddict[key1] = value1

    return ddict

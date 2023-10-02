"""The get_all_values() function takes two arguments in the following order:

chainmap - an object of type ChainMap, the elements of which are dictionaries
key - arbitrary object

The function returns a set whose elements are all values for the key 'key' from
all dictionaries in the chainmap. If key is not in the chainmap,
the function returns an empty set."""

from collections import ChainMap


def get_all_values(chainmap: ChainMap, key: str) -> set:
    arr = []
    for i in chainmap.maps:
        for k, v in i.items():
            if k == key:
                arr.append(v)
    return set(arr)

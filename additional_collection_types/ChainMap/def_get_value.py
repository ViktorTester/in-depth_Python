"""The get_value() function takes three arguments in the following order:

chainmap - an object of type ChainMap, the elements of which are dictionaries
key - arbitrary object
from_left — boolean value, defaults to True

The function will return the value of the key from the chainmap, and:

if 'from_left' is True, the key lookup in the chainmap proceeds from the first dictionary to the last
if 'from_left' is False, the key lookup in the chainmap proceeds from the last dictionary to the first
If key is not in the chainmap, the function will return None."""

from collections import ChainMap


def get_value(chainmap: ChainMap, key: str, from_left=True) -> str or None:
    if key in chainmap.keys():
        if from_left:
            for k, v in chainmap.items():
                if k == key:
                    return v
        else:
            for i in reversed(chainmap.maps):
                for k, v in i.items():
                    if k == key:
                        return v
    return None

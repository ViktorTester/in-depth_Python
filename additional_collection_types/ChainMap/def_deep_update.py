"""The deep_update() function takes three arguments in the following order:

chainmap - an object of type ChainMap, the elements of which are dictionaries
key - hashable object
value - arbitrary object

The function changes all values by key in all dictionaries in the chainmap to value.
If key is not in the chainmap, the function adds the key: value pair to the first dictionary."""

from collections import ChainMap


def deep_update(chainmap: ChainMap, key: str, value: str) -> None:
    if key in chainmap.keys():
        for i in chainmap.maps:
            for k, v in i.items():
                if k == key:
                    i[k] = value
    else:
        chainmap.maps[0][key] = value

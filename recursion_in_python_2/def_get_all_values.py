"""The get_all_values() function takes two arguments in the following order:

nested_dicts - a dictionary containing arbitrary objects or dictionaries as values,
which, in turn, also contain arbitrary objects or dictionaries as values;
nesting can be arbitrary

key - hashable object

The function determines all the values that match the key in the nested_dicts
dictionary and all its nested dictionaries, and returns them as a set.
If key is not in any dictionary, the function returns an empty set."""

from typing import Any


def get_all_values(nested_dicts: dict, key: Any) -> set:
    result = set()
    if key in nested_dicts:
        result.add(nested_dicts[key])

    for v in nested_dicts.values():
        if isinstance(v, dict):
            result.update(get_all_values(v, key))
    return result

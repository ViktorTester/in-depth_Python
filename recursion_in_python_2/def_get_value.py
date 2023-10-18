"""The get_value() function takes two arguments in the following order:

nested_dicts - a dictionary containing arbitrary objects or dictionaries
as values, which, in turn, also contain arbitrary objects
or dictionaries as values; nesting can be arbitrary

key - hashable object

The function determines the value that matches the key in the nested_dicts
dictionary or one of its nested dictionaries, and returns the resulting result."""

from typing import Any


def get_value(nested_dicts: dict, key: Any) -> Any | None:
    if key in nested_dicts:
        return nested_dicts[key]

    for v in nested_dicts.values():
        if isinstance(v, dict):
            value = get_value(v, key)
            if value is not None:
                return value
    return None

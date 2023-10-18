"""The dict_travel() function takes one argument:

nested_dicts - a dictionary containing numbers, strings or dictionaries
as values, which, in turn, also contain numbers, strings or dictionaries
as values; nesting can be arbitrary

The function prints all the key-value pairs of the nested_dicts dictionary,
as well as the values of all its child dictionaries. When displaying
the values of child dictionaries, the function enumerates the names
of all keys, starting from the top level, separating them with dots."""


def dict_travel(nested_dicts: dict, prefix: str = '') -> None:
    for key in sorted(nested_dicts.keys()):
        value = nested_dicts[key]
        if isinstance(value, dict):
            dict_travel(value, f"{prefix}.{key}" if prefix else f"{key}")
        else:
            if prefix:
                print(f"{prefix}.{key}: {value}")
            else:
                print(f"{key}: {value}")

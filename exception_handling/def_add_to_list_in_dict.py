"""The add_to_list_in_dict() function takes three arguments in the following order:

data - dictionary of lists
key - hashable object
element - arbitrary object

The function adds an element object to the list by key in the 'data' dictionary.
If the key is not in the 'data' dictionary, the function adds it to the dictionary,
assigns an empty list as its value, and adds an element object to that list."""

from typing import Dict, Hashable, Any, List


def add_to_list_in_dict(data: Dict[Hashable, List[Any]], key: Hashable, element: Any) -> None:
    try:
        data[key].append(element)
    except KeyError:
        data[key] = [element]

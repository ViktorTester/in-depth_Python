"""The custom_sort() function sorts the ordered_dict dictionary:

by keys if by_values is False
by values if by_values is True"""

from collections import OrderedDict


def custom_sort(ordered_dict: OrderedDict, by_values=False) -> None:
    if by_values:
        for key in sorted(ordered_dict, key=lambda x: ordered_dict[x]):
            ordered_dict.move_to_end(key)
    else:
        for key in sorted(ordered_dict):
            ordered_dict.move_to_end(key)

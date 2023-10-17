"""The recursive_sum() function takes one argument:

nested_lists - a list whose elements are integers or lists,
the elements of which, in turn, are also either integers or lists;
nesting can be arbitrary.

The function calculates the sum of all numbers in all lists and
returns the result. If nested_lists is empty, the function returns 0."""


def recursive_sum(nested_lists: list) -> int:
    if not nested_lists:
        return 0
    else:
        total_sum = 0
        for item in nested_lists:
            if isinstance(item, list):
                total_sum += recursive_sum(item)
            elif isinstance(item, int):
                total_sum += item
        return total_sum

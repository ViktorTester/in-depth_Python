"""Linearization is the process of transforming a list, which may contain
several levels of nested lists, into a list containing
all the same elements without any nesting.

The linear() function takes one argument:

nested_lists - a list whose elements are integers or lists,
the elements of which, in turn, are also either integers or
lists; nesting can be arbitrary.

The function returns a new list, which is a linearized list of nested_lists."""


def linear(nested_lists: list) -> list:
    result = []
    for i in nested_lists:
        if isinstance(i, list):
            result.extend(linear(i))
        else:
            result.append(i)
    return result

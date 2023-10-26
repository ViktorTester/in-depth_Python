"""The sort_priority() function takes two arguments in the following order:

values — list of numbers
group — list, tuple or set of numbers

The function sorts the list of numbers values in non-descending order,
while giving priority to the group of numbers from group that should come first."""


def sort_priority(values: list, group: list or set or tuple) -> list:
    arr = values[:]
    values.clear()
    for i in sorted(arr):
        if i in group:
            values.append(i)
            arr.remove(i)
    values.extend(sorted(arr))
    return values

"""The index_of_nearest function finds the closest number
to number in the numbers list and returns its index.
If the numbers list is empty, the function returns the number −1."""


def index_of_nearest(numbers: list, number: int) -> int:
    minimal = 999
    if not numbers:
        return -1
    else:
        ind = 0
        for index, value in enumerate(numbers):
            dif = abs(value - number)
            if dif < minimal:
                minimal = dif
                ind = index

        return ind
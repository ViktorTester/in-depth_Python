"""The polynom() function takes one argument:

x — real number

The function returns the value of the expression x** 2 - 1

The function also has a values attribute, which is a set (set type)
of all function values that have already been calculated."""


def polynom(x: int) -> int:
    answer = x ** 2 + 1
    polynom.values = polynom.values | {answer}

    return answer


polynom.values = set()

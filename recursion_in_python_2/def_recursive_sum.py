"""The recursive_sum() function takes two arguments in the following order:

a — non-negative integer
b — non-negative integer

The function calculates the sum of numbers 'a' and 'b'.
When calculating the sum, the function:

doesn't use loops
of all arithmetic operations uses only +1 and −1"""


def recursive_sum(a: int, b: int or float) -> int:
    if b == 0:
        return a
    return recursive_sum(a + 1, b - 1)

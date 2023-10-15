"""The get_pow() function takes two arguments in the following order:

a — positive integer
n — non-negative integer

The function calculates the value of 'a' to the power of 'n' and returns the result."""


def get_pow(a: int, n: int) -> int:
    if n == 0:
        return 1
    return a * get_pow(a, n - 1)

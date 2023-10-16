"""The get_fast_pow() function takes two arguments in the following order:

a is a positive integer
n — non-negative integer

The function calculates the value of 'a' to the power of 'n' using
the fast exponentiation algorithm and returns the result."""


def get_fast_pow(a: int, n: int or float) -> int:
    if n == 0:
        return 1
    elif n % 2 == 1:
        return a * get_fast_pow(a, n - 1)
    return get_fast_pow(a * a, n / 2)

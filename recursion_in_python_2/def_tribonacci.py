"""Tribonacci sequence is a sequence of natural numbers,
where each subsequent number is the sum of the three previous ones.

The tribonacci() function takes one argument:

n - natural number

The function, using recursion and memoization,
returns True if number is a power of 2, or False otherwise."""

cache = {1: 1, 2: 1, 3: 1}


def tribonacci(n: int) -> int:
    result = cache.get(n)
    if result is None:
        result = tribonacci(n - 2) + tribonacci(n - 1) + tribonacci(n - 3)
        cache[n] = result
    return result

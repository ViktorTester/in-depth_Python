"""The primes() generator function takes two arguments in the following order:

left — natural number
right — natural number

The function returns a generator that generates a sequence of prime
numbers from left to right, inclusive, and then raises a 'StopIteration' exception.

It is guaranteed that 'left' <= 'right'.

A prime number is a natural number that has exactly two distinct
natural divisors: one and itself. One is not a prime number."""


def primes(left, right):
    for i in range(left, right + 1):
        counter = 0
        if i > 1:
            for j in range(2, i + 1):
                if i % j == 0:
                    counter += 1
            if counter == 1:
                yield i
        else:
            continue

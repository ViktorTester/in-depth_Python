"""A generator function palindromes() that takes no arguments.

The function returns a generator that generates an infinite
sequence of natural palindromic numbers."""


def palindromes():
    num = 0
    while True:
        num_str = str(num)
        if num_str == num_str[::-1]:
            yield num
        num += 1


generator = palindromes()
numbers = [next(generator) for _ in range(30)]

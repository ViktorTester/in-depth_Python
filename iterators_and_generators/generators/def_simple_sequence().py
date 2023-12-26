"""The generator function simple_sequence() does not accept any arguments.

The function returns a generator that generates an infinite increasing
sequence of natural numbers, in which each number occurs as many times
as it is: 1,2,2,3,3,3,4,4,4,4..."""


def simple_sequence():
    number = 1
    while True:
        for _ in range(number):
            yield number
        number += 1


generator = simple_sequence()
numbers = [next(generator) for _ in range(30)]

print(*numbers)

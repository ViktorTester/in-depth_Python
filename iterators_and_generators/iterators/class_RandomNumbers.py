"""The 'RandomNumbers' class generates iterators, and its
constructor takes three arguments in the following order:

left — integer
right — integer
n - natural number

The 'RandomNumbers' class iterator generates a sequence of 'n' random
numbers from 'left' to 'right', inclusive,
and then raises a StopIteration exception.

It is guaranteed that left <= right."""

from random import randint as r


class RandomNumbers:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.n = n
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            self.count += 1
            return r(self.left, self.right)
        else:
            raise StopIteration

"""The 'Fibonacci' class generates iterators; its constructor does not take any arguments.

The Fibonacci class iterator generates an infinite sequence of Fibonacci numbers, starting with 1."""


class Fibonacci:
    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        result = self.curr
        self.curr, self.prev = self.curr + self.prev, self.curr
        return result

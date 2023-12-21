"""The 'Cycle' class generates iterators, its constructor takes one argument:

iterable — iterable object

The 'Cycle' class iterator cyclically generates
a sequence of elements of an iterable object.

It is guaranteed that the 'iterable' object passed to
the class constructor is not a set or an iterator."""


class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.counter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        if self.counter == len(self.iterable):
            self.counter = 0
        return self.iterable[self.counter]


cycle = Cycle(range(100_000_000))

print(next(cycle))
print(next(cycle))

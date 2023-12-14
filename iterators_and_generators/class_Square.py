"""The 'Square' class generates iterators, its constructor takes one argument:

n - natural number

The Square class iterator generates a sequence of 'n' numbers,
each of which is the square of a different natural number,
and then raises a StopIteration exception."""
class Square:
    def __init__(self, n: int):
        self.n = n
        self.current = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            square = self.current ** 2
            self.current += 1
            self.count += 1
            return square
        else:
            raise StopIteration

squares = Square(10)

print(list(squares))
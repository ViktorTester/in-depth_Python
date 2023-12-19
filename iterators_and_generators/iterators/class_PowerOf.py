"""The 'PowerOf' class generates iterators, its constructor takes one argument:

number - non-zero number

The PowerOf class iterator generates an infinite sequence of integer
non-negative powers of 'number' in ascending order, starting with power zero."""
class PowerOf:
    def __init__(self, number):
        self.number = number
        self.power = 0

    def __iter__(self):
        return self

    def __next__(self):
        result = self.number ** self.power
        self.power += 1
        return result
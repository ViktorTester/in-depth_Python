"""The 'Xrange' class generates iterators, its constructor
takes three arguments in the following order:

start — integer or real number
end — integer or real number
step — integer or real number, default value is 1

The Xrange class iterator generates a sequence of members of the arithmetic
progression from 'start' to 'end', including 'start' and not including 'end',
with step 'step', and then raises a StopIteration exception."""


class Xrange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0 and self.current < self.end or self.step < 0 and self.current > self.end:
            result = self.current
            self.current += self.step
            return result
        else:
            raise StopIteration

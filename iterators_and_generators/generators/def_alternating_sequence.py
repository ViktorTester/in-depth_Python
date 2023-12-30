"""The generator function alternating_sequence() takes one argument:

count - natural number, default value is None

If 'count' is None, the function returns a generator that produces
an infinite-sign alternating series of natural numbers.

If 'count' has a natural number as its value, the function returns a
generator that generates the first count numbers of an alternating
series of natural numbers, and then raises a StopIteration exception."""


def alternating_sequence(count=None):
    current_num = 1
    generated_count = 0
    sign = 1

    while count is None or generated_count < count:
        yield current_num * sign
        generated_count += 1

        current_num += 1
        sign *= -1

"""The calculate_it() function takes one or more
arguments in the following order:

func - arbitrary function
*args - a variable number of positional arguments,
each of which is an arbitrary object

The function returns a tuple whose first element is the return
value of func when called with arguments *args, and the second
element is the approximate time (in seconds)
it took to calculate this value."""

import time


def add(a, b, c):
    time.sleep(3)
    return a + b + c


def calculate_it(func, *args):
    start_time = time.monotonic()
    value = func(*args)
    end_time = time.monotonic()
    elapsed_time = end_time - start_time
    return value, elapsed_time


print(calculate_it(add, 1, 2, 3))

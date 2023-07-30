"""The get_the_fastest_func() function takes two
arguments in the following order:

funcs - list of arbitrary functions
arg - arbitrary object

The get_the_fastest_func() function returns the function
in the funcs list that took the least amount of time
to compute the value when called with arg."""

import time


def get_the_fastest_func(x: list, arg):
    d = {}
    for i in range(len(x)):
        start_time = time.monotonic()
        x[i](arg)
        end_time = time.monotonic()
        time_dif = end_time - start_time
        d[x[i]] = time_dif

    min_time = 9999
    for key, value in d.items():
        if value < min_time:
            min_time = value
            min_func = key
    return min_func

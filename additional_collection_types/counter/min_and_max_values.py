"""There is a data variable containing the Counter dictionary.
The program adds two attributes to this dictionary:

min_values() - a function that returns a list of elements with the smallest value
max_values() - a function that returns a list of elements with the highest value"""

from collections import Counter


def min_values():
    arr2 = dict(data.most_common())
    min_values = [(key, value) for key, value in arr2.items() if value == min(arr2.values())]

    return min_values


def max_values():
    arr = dict(data.most_common())
    max_values = [(key, value) for key, value in arr.items() if value == max(arr.values())]

    return max_values


data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.min_values = min_values
data.max_values = max_values

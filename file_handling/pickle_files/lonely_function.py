"""There is a pickle file containing a single serialized function.
The program calls the given function with the given arguments
and prints the function's return value."""

import pickle
import sys

fname, *args = [i.strip() for i in sys.stdin]

with open(fname, 'rb') as fin:
    function = pickle.load(fin)

print(function(*args))

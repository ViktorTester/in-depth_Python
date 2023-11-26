"""The program takes an arbitrary number of English words as
input and arranges the letters in each one in lexicographic order."""

import functools
import sys


@functools.lru_cache
def return_this(word):
    return ''.join(sorted(list(word)))


arr = [line.strip('\n') for line in sys.stdin]

for i in arr:
    print(return_this(i))

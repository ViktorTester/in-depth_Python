"""The program displays words consisting of two identical syllables.

An arbitrary number of words are given as input to the program, each on a separate line.

From the entered words, the program displays only those that consist of two identical syllables.
The words are in their original order, each on a separate line.

A word is any continuous sequence of one or more characters matching '\w'."""

import sys
from re import fullmatch

pattern = r'^(\w+)\1$'

for i in sys.stdin:
    n = i.strip('\n')

    match = fullmatch(pattern, n)

    if match:
        print(n)

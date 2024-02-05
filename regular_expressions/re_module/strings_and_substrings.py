"""""The program defines:

-number of lines in which 'hello' appears as a substring at least twice
-number of lines in which 'world' appears as a word at least once

The input to the program is an arbitrary number of lines,
each of which contains a set of arbitrary characters.

The program displays two numbers:

-the first is the number of lines in which 'hello' appears as a substring at least twice
-the second is the number of lines in which 'world' appears as a word at least once
each on a separate line.

A word is any continuous sequence of one or more characters matching '\w'."""

import sys
from re import findall

pattern1 = r'bee'
pattern2 = r'\bgeek\b'

counter1 = 0
counter2 = 0

for i in sys.stdin:

    n = i.strip('\n')

    match1 = findall(pattern1, n)
    match2 = findall(pattern2, n)

    if len(match1) > 1:
        counter1 += 1
    if len(match2) > 0:
        counter2 += 1

print(counter1)
print(counter2)

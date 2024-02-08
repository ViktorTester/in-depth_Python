"""An arbitrary number of lines are given as input to the program.
The program determines how many publications contain the string 'hello'."""

import sys
import re

pattern = r'hello'
counter = 0

for i in sys.stdin:
    n = i.strip('\n')

    match = re.search(pattern, n, re.I)

    if match:
        counter += 1

print(counter)

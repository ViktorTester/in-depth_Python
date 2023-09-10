"""There is a block of code in Python. The program removes all
lines in the given code that contain only comments. If there
is something else in the line besides the comment,
then this line is not taken into account."""


import sys

data = [line.strip('\n') for line in sys.stdin]


for i in data:
    if i.strip().startswith('#'):
        continue
    print(i)

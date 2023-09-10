"""There is a sequence of integers.
The program determines whether the given sequence
is a progression, and if so, determines its form."""

import sys

data = [line.strip('\n') for line in sys.stdin]

plus = []
divide = []

for i in range(1, len(data)):
    plus.append(int(data[i]) - int(data[i - 1]))
    divide.append(int(data[i]) / int(data[i - 1]))

if len(set(plus)) == 1:
    print('Arithmetic progression')
elif len(set(divide)) == 1:
    print('Geometric progression')
else:
    print('Not a progression')

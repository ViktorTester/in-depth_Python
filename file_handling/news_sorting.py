"""The program receives an arbitrary number of lines as input,
each line, except for the last line, contains news, the category
to which it belongs, and its reliability in the following format:

<news> / <category> / <credibility>

The last line contains a single category.


The program displays all the news that belong to the entered category.
The news are arranged in order of increasing degree of certainty,
and if the degrees of certainty coincide,
in the lexicographic order of the news itself."""

import sys

data = [line.strip('\n').split(' / ') for line in sys.stdin]
news = data[-1]
arr = [i[0] + ' ' + i[2] for i in data[:-1] if [i[1]] == news]

for j in sorted(arr, key=lambda x: (float(x[-3:]), x)):
    print(j[:-4])

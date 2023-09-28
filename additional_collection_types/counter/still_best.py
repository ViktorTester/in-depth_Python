"""There is a list of students' names and their exam grades.
The program determines the second student with the lowest grade."""

from collections import Counter
import sys

d = {}
for line in sys.stdin:
    s = line.strip('\n').split()
    d[s[0]] = int(s[1])

marks = Counter(d)
print(marks.most_common()[-2][0])

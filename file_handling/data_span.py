"""There is a sequence of dates. The program displays the number
of days between the maximum and minimum dates of the given sequence."""

import sys
from datetime import datetime

arr = []
for line in sys.stdin:
    days = line.strip().split('-')
    arr.append(datetime(int(days[0]), int(days[1]), int(days[2])))

answer = (max(arr) - min(arr))
print(answer.days)

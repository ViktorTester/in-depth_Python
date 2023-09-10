"""The program receives an arbitrary number of lines (two or more)
as input, each line contains a date in the format DD.MM.YYYY.

The program outputs the text:

ASC - if the dates in the entered sequence are in ascending order.
DESC - if the dates in the entered sequence are in descending order.
MIX - if the dates in the entered sequence are neither ascending
nor descending, or the sequence contains duplicate dates."""

import sys
from datetime import date

data = [list(map(int, line.strip('\n').split('.'))) for line in sys.stdin]

arr = [date(i[2], i[1], i[0]) for i in data]

if len(set(arr)) == len(data):
    if arr == sorted(arr):
        print('ASC')
    elif arr == sorted(arr, reverse=True):
        print('DESC')
    else:
        print('MIX')
else:
    print('MIX')

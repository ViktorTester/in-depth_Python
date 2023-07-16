"""The program takes two dates as input
and outputs the smaller one."""

from datetime import date

arr = []
try:
    for _ in range(2):
        year, month, day = input().split('-')
        arr.append(date(int(year), int(month), int(day)))
except ValueError:
    print('Input error')

print(min(arr).strftime('%d-%m (%Y)'))

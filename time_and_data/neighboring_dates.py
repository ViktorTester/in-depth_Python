"""There is a sequence of dates. The program creates and displays
a list whose elements are non-negative integers — the number
of days between two adjacent dates in the sequence."""

from datetime import date

s = input().split()
arr, result = [], []

for i in s:
    day, month, year = i.split('.')
    my_date = date(int(year), int(month), int(day))
    arr.append(my_date)

for j in range(1, len(arr)):
    result.append((abs(arr[j] - arr[j - 1])).days)

print(result)
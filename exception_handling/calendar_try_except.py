"""The program displays the name of the month corresponding
to the entered integer (from 1 to 12 inclusive)"""

from calendar import month_name

d = {}
counter = 0

for i in month_name[1:]:
    counter += 1
    d[i] = counter

try:
    n = int(input())
    if 1 <= n <= 12:
        pass
    else:
        print('The number entered is from an invalid range')
except:
    print('Invalid value')
else:
    for key, value in d.items():
        if n == value:
            print(key)

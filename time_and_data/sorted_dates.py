"""The program takes a sequence of dates as input and outputs
them in non-decreasing order in the DD/MM/YYYY format."""

from datetime import date

arr = []
for i in range(n := int(input())):
    year, month, day = input().split('-')
    my_date = date(int(year), int(month), int(day))
    arr.append(my_date)

result = [j.strftime('%d/%m/%Y') for j in sorted(arr)]

for x in result:
    print(x)

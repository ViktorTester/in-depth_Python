"""The program adds all natural numbers in
a string that are in the specified index range.

The input to the program is first given two integers 'a' and 'b',
greater than or equal to 0, separated by a space, and then a string."""

import re

a, b = map(int, input().split())
s = input()

regex_obj = re.compile('\d+')

arr = regex_obj.findall(s, pos=a, endpos=b)

print(sum(map(int, arr)))

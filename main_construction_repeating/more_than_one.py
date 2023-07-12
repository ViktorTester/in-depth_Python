"""You are given a sequence of non-negative
integers. The program displays those numbers
that occur more than once in the given sequence."""

s = input().split()
d = {}

for i in s:
    d[i] = d.get(i, 0) + 1

arr = [int(key) for key, value in d.items() if value > 1]

print(*(sorted(arr)))

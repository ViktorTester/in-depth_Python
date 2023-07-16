"""There is a sequence of natural numbers from 1 to n inclusive.
The program groups all the numbers in a given sequence by the sum
of their digits and determines the length of the
group containing the largest number of numbers."""

arr = list(map(str, range(1, n := int(input()) + 1)))

arr_sum = list(map(lambda x: sum(map(int, x)), map(str, arr)))

final_arr = list(map(str, arr_sum))

d = {}
for i in final_arr:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d.get(i, 0) + 1

max_value = 0
for value in d.values():
    if value > max_value:
        max_value = value

print(max_value)

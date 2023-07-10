"""The input to the program is a natural number 'n'.
Each of the following n-lines, separated by a comma and
a space, contains a list of languages that the person knows.
If there are languages that are known to each of 'n' people,
the program displays them as a result, if there are no such
languages, the program displays the
inscription "No common languages"."""

arr, final, d = [], [], {}

for i in range(n := int(input())):
    arr.append(input().split(', '))

for x in range(len(arr)):
    for y in range(len(arr[x])):
        counter = arr[x].count(arr[x][y])
        if arr[x][y] not in d.keys():
            d[arr[x][y]] = counter
        else:
            d[arr[x][y]] = d.get(arr[x][y], 0) + 1

for key, value in d.items():
    if value == n:
        final.append(key)

if len(final) > 0:
    final.sort()
    print(*final, sep=', ')
else:
    print('No common languages')
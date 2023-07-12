"""There is a house and two shops near it. There is a path between
the first store and the house and a path between the second store
and the house, and there is also a common road connecting the two
stores. The route starts at home and ends at home. The program
calculates the minimum distance required to visit both stores
and return home. It is allowed to visit the same store or walk
on the same path more than once. The only task is to minimize
the total distance travelled.

Input data format
The program receives 3 natural numbers as input: a, b, c -
the lengths of the tracks, each on a separate line:
'a' is the length of the path connecting the house and the first store
'b' - the length of the path connecting the house and the second store
c is the length of the track connecting the shops"""

values = [int(input()) for _ in range(3)]
a, b, c = values

total = sum(values)

pos = values.index(max(values))
n = values.pop(pos)
two_min = sum(values) * 2

print(min(total, two_min))

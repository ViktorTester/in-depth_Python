"""There is a sequence of natural numbers from 1 to n. The program
first reverses some elements of this sequence from element
number X to element number Y, and then from
element number A to element number B.
The program receives 5 natural numbers
separated by a space: n, X, Y, A, B"""

values = list(map(int, input().split()))
n, X, Y, A, B = values
arr = list(range(1, n + 1))

arr[X - 1: Y] = reversed(arr[X - 1: Y])
arr[A - 1: B] = reversed(arr[A - 1: B])

print(*arr)
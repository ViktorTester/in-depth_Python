"""The program determines the minimum and maximum values of
a function on a segment in integer points.

Input format:

The correct function f(x) is supplied as input to the program in the first line;
in the next line two integers 'a' and 'b' are entered, separated by a space,
which represent the boundaries of the segment [a;b]."""

code = '''n = input()
ab = list(map(int, input().split()))
arr = []

for x in range(ab[0], ab[1] + 1):
    arr.append(eval(n))

interval = str(ab).replace(",", ";")

print(f'The minimum value of the function {n} on the interval {interval} is {min(arr)}')
print(f'The maximum value of the function {n} on the interval {interval} is {max(arr)}')'''

exec(code)

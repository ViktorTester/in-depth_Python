"""The program takes as input an arbitrary number of lines containing
correct mathematical expressions and displays the value of the largest of them."""

code = '''import sys

data = [line.strip() for line in sys.stdin]

print(max(map(eval, data)))'''

exec(code)

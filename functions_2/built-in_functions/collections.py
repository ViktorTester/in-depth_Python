"""The program takes as input a valid non-empty list, a valid non-empty tuple,
or a valid set of arbitrary length, and does the following:

if a list is entered, displays its last element
if a tuple is entered, outputs its first element
if a set is entered, displays the number of its elements"""

code = '''n = eval(input())
if isinstance(n, list):
    print(n[-1])
elif isinstance(n, tuple):
    print(n[0])
elif isinstance(n, set):
    print(len(n))'''
exec(code)

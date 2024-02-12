"""The program swaps the first two letters in each word consisting of two or more letters.

The input to the program is a string containing words.

The program, in the input line, replaces the first two letters in each
word consisting of two or more letters, and displays the result."""

import re

s = input()


def func(match_obj):
    s = match_obj.group(0)
    if len(s) >= 2:
        return s[1] + s[0] + s[2:]
    return s


result = re.sub(r'\b\w+\b', func, fr'{s}')

print(result)

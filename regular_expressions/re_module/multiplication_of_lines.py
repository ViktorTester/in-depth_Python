"""Let's call multiplication of a string by a number an entry in the format n(string),
where 'n' is a non-negative integer, and string is a string that must be written 'n' times.
We will consider the expansion of the multiplication to be the expanded version of
this record, for example, the line ti2(Be)3(Ge) after expanding
all the multiplications in it will have the form tiBeBeGeGeGe.

The program reveals all the multiplications in the text and displays the result."""

import re


def expand_multiplications(s):
    pattern = r'(\d+)\(([^()]+)\)'

    def replace_multiplication(match):
        n = int(match.group(1))
        substring = match.group(2)
        return n * substring

    while re.search(pattern, s):
        s = re.sub(pattern, replace_multiplication, s)

    return s


text = input()

print(expand_multiplications(text))

"""In Python, there are keywords that cannot be used to name variables, functions, and classes.

The program takes a string of text and replaces all keywords in it with <kw>."""

import re
import keyword

s = input()

for i in keyword.kwlist:
    s = re.sub(fr'\b{i}\b', r'<kw>', s, flags=re.I)

print(s)

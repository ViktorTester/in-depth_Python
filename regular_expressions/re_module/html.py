"""A hyperlink consists of two parts - a pointer and an address part.
A link pointer is a piece of text or image visible to the user.
The address part of the link is not visible to the user;
it represents the address of the resource to which you need to go.
Sometimes the pointer may be surrounded by various tags.

The program finds all hyperlinks in a fragment of an HTML
page and displays their components - address parts and pointers.

The program receives an arbitrary number of lines as input,
which form a fragment of an HTML page."""

import sys
import re

pattern = r'<a\s+href="([^"]+)">((?:<\w+>)*([^<]+)(?:<\/\w+>)*)<\/a>'

for i in sys.stdin:

    n = i.strip('\n')

    match = re.findall(pattern, n)

    for n in match:
        print(f'{n[0]}, {n[1]}')

"""In an online school, an account login is determined as follows:

-The first character is the underscore character '_'
-followed by one or more digits
-after zero or more Latin letters are written in any case
-login may end with an optional underscore character '_'

The program takes an arbitrary number of lines and determines
which of them represent the correct online school login."""

import sys
from re import fullmatch

pattern = r'^_\d+[a-zA-Z]*_?$'

for i in sys.stdin:
    n = i.strip('\n')

    match = fullmatch(pattern, n)

    if match:
        print(True)
    else:
        print(False)

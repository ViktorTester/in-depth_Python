"""There is a set of telephone numbers having the following formats:

<country code>-<city code>-<number>
<country code> <city code> <number>

in which the country code and city code are represented by sequences of one to three
digits, inclusive, and the number is represented by a sequence of four to ten digits,
inclusive. Between the country code, city code and number, a separator is used,
which is either a hyphen or a space, and both types of separator cannot
be present in one number at the same time.

The program accepts an arbitrary number of phone numbers and for each one
it displays separately its country code, city code and number."""

import sys
from re import search

pattern = r'(?P<w1>\d{1,3})([ -])(?P<w2>\d{1,3})\2(?P<w3>\d{4,10})'

for i in sys.stdin:
    n = i.strip('\n')

    match = search(pattern, n)
    if match:
        a = match.groupdict()
        print(f'Country code: {a["w1"]}, City code: {a["w2"]}, Number: {a["w3"]}')
    continue

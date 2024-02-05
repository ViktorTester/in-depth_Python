"""The Online school monitors their popularity. To do this, they collect publications
from various social networks that contain occurrences of the string 'hello' in lowercase.
The publication is evaluated:

-3 points if it starts and ends with the line 'hello'
-2 points if it just starts or just ends with the line 'hello'
-1 point if it contains the string 'hello' only inside
-0 points if it does not contain the string 'hello'

The program determines the popularity of an online school
by summing the scores of all publications.

The program receives an arbitrary number of lines as input,
each of which represents the next publication.

The program determines how many points each entered publication
is worth and displays the sum of all points received."""

import sys
import re

pattern1 = r'^hello'
pattern2 = r'hello$'
pattern3 = r'hello'
pattern4 = r'^hello'

counter = 0

for i in sys.stdin:

    n = i.strip('\n')

    if re.search(pattern1, n) and re.search(pattern2, n):
        counter += 3
    elif re.search(pattern1, n) or re.search(pattern2, n):
        counter += 2
    elif re.search(pattern3, n):
        counter += 1
    elif re.search(pattern4, n):
        continue

print(counter)

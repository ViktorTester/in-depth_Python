"""The program receives an indefinite number of lines as input,
each of which contains an arbitrary value. The program displays the sum of
all numbers entered, and then the number of non-numeric values entered."""

import sys

total = 0
word_count = 0

for i in sys.stdin:
    try:
        try:
            total += int(i)
        except:
            total += float(i)
    except (TypeError, ValueError):
        word_count += 1


print(total)
print(word_count)
"""There is a sequence of words.
The program groups words from this sequence according to their
length and determines the number of words in each resulting group."""

from collections import Counter

s = input().lower().split()

arr = [len(i) for i in s]

for key, value in sorted(Counter(arr).items(), key=lambda x: x[1]):
    print(f'Words {key} in length - {value} pieces')

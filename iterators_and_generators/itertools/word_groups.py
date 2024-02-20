"""The program groups the entered words by their length and displays the
resulting groups. For each group, the length is indicated, and then the words
that have the corresponding length are listed, separated by commas.
Groups are arranged in order of increasing length, each on a
separate line, words in groups are in alphabetical order"""

from itertools import groupby

words = sorted(input().split(), key=lambda x: len(x))

grouped_words = groupby(words, key=lambda x: len(x))

for key, value in grouped_words:
    arr = [i for i in value]
    print(f'{key} -> {", ".join(sorted(arr))}')

"""There is a sequence of words. The program displays the least frequently
occurring word in this sequence. If there are several such words,
the program displays them all."""

from collections import Counter

s = Counter(input().lower().split())

rare_word = s.most_common()[-1][1]

arr = [i[0] for i in s.most_common() if i[1] == rare_word]

x = sorted(arr)

for j in x:
    print(j, end=', ' if j != x[-1] else '\n')

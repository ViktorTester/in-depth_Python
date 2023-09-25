"""There is a text file 'pythonzen.txt' containing text in English.
The program determines how many times each letter appears in this text.
Letters and their number are displayed in lexicographic order,
each on a separate line"""

from collections import Counter

with open('pythonzen.txt', encoding='utf-8') as file:
    text = list(map(str.strip, file.readlines()))

    arr = [j.lower() for i in text for j in i if j.isalnum()]

    for key, value in sorted(Counter(arr).items()):
        print(f'{key}: {value}')

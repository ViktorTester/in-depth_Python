"""The print_bar_chart() function takes two arguments in the following order:

'data' — string or list of strings
'mark' - single character

The function determines how many times each character appears in a string or list.

The function then displays the result as a bar graph, indicating each character (line)
and its number. The quantity is displayed as repeating
the 'mark' symbol the corresponding number of times"""

from collections import Counter


def print_bar_chart(data: str or list, mark: str) -> None:
    ct = Counter(data)
    top_len = len(max(ct, key=len))

    for key, value in sorted(ct.items(), key=lambda x: x[1], reverse=True):
        print(f'{key.ljust(top_len)} |{value * mark}')

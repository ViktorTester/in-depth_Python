"""The program takes as input a line of text and a word and determines
how many times this word occurs as a subword in the entered text.

The input to the program is text on the first line, and a word on the second line.

The program determines how many times a given word occurs
as a subword in the entered text and displays the result."""

import re

text, word = input(), input()

pattern = fr'\B{word}\B'

match = re.findall(pattern, text)

print(match)

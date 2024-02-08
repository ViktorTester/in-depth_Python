"""American English and British English have several differences,
one of which is in the spelling of words. For example, words written
in American English with the suffix 'ze' are often written
using the suffix 'se' in British English.

The program determines how many times a word appears in the text,
taking into account its British-American spelling.


The input to the program on the first line is a word that can be
written in both British and American versions, and on the next line - text.


The program determines how many times the entered word appears in the text,
taking into account its British-American spelling, and displays the result."""

import re

word, text = input(), input()

pattern = fr'\b{word[:-2]}[zs]e'

match = re.findall(pattern, text, re.I)

print(len(match))

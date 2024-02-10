"""The abbreviate() function takes one argument:
'phrase' - phrase

The function creates an uppercase abbreviation from the 'phrase' phrase and returns it.

The abbreviation takes into account both the initial letters of words and the initial
letters of subwords that begin with a capital letter,
for example, JavaScript Object Notation -> JSON."""

import re


def abbreviate(text):
    pattern = r'\b(\w)|\B([A-Z]+)'

    match = re.finditer(pattern, text)

    arr = [i.group().capitalize() for i in match]

    return ''.join(arr)


print(abbreviate('javaScript object notation'))

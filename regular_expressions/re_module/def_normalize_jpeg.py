"""The normalize_jpeg() function takes one argument:

filename - file name with .jpeg or .jpg extension,
which can be written in arbitrary case letters

The function returns the new file name with a normalized extension - .jpg."""

import re


def normalize_jpeg(filename: str):
    res = re.sub(r'jpeg$|jpg$', r'jpg', filename, flags=re.I)
    return res


print(normalize_jpeg('jpg.jPg.Jpg.JPG'))

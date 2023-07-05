"""The convert() function returns a string:

completely lowercase if there are more
lowercase letters in this string

fully uppercase if there are more
uppercase letters in this string

entirely lowercase if the number of uppercase and
lowercase letters in this string is the same"""


def convert(string: str) -> str:
    counter_low = 0
    counter_up = 0

    for i in string:
        if i.islower():
            counter_low += 1
        elif i.isupper():
            counter_up += 1

    if counter_up > counter_low:
        return string.upper()
    elif counter_low >= counter_up:
        return string.lower()
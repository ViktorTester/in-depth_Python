"""Let's call a password good if:

its length is 9 or more characters
it contains large and small letters of any alphabet
it contains at least one digit

The EAFP-style is_good_password() function takes one argument:

string — arbitrary string

The function returns True if string is a good password, or raise an exception:

LengthError if its length is less than 9 characters
LetterError if there are no letters or all letters are the same case
DigitError if there are no digits in it"""


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(string: str) -> bool:
    c_upper = 0
    c_lower = 0
    c_digit = 0

    for i in string:
        if i.isupper():
            c_upper += 1
        elif i.islower():
            c_lower += 1
        elif i.isdigit():
            c_digit += 1

    if len(string) < 9:
        raise LengthError

    if c_upper < 1 or c_lower < 1:
        raise LetterError

    if c_digit < 1:
        raise DigitError

    return True

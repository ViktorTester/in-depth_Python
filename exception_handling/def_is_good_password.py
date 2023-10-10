"""Let's call a password good if:

its length is 9 or more characters
it contains large and small letters of any alphabet
it contains at least one digit

The program requires you to enter a new password until a good one is entered.

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


def is_good_password(string: str) -> LengthError | LetterError | DigitError | str:
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

    try:
        if len(string) < 9:
            raise LengthError('LengthError')
        if c_upper < 1 or c_lower < 1:
            raise LetterError('LetterError')
        if c_digit < 1:
            raise DigitError('DigitError')
    except LengthError as len_e:
        return len_e
    except LetterError as let_e:
        return let_e
    except DigitError as d_e:
        return d_e
    else:
        return 'Success!'


while True:
    result = is_good_password(input())
    if result == 'Success!':
        print(result)
        break
    else:
        print(result)

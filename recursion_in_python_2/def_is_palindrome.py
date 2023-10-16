"""The is_palindrome() function takes one argument:

string — arbitrary string

The function returns True if the passed string
is a palindrome, or False otherwise."""


def is_palindrome(string: str) -> bool:
    if len(string) <= 1:
        return True
    else:
        if string[0] == string[-1]:
            return is_palindrome(string[1:-1])
        else:
            return False

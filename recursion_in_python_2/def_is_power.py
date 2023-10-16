"""The is_power() function takes one argument:

number - natural number

The function returns True if number is a power of 2, or False otherwise."""


def is_power(number: int or float) -> bool:
    if number == 1 or number == 2:
        return True
    else:
        if 2 <= number:
            return is_power(number / 2)
        else:
            return False

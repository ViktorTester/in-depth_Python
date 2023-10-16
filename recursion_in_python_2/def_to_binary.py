"""The to_binary() function takes one argument:

number — non-negative integer

Function representing the number 'number' in the binary number system."""


def to_binary(number: int) -> str:
    if number <= 1:
        return str(number)
    return to_binary(number // 2) + str(number % 2)

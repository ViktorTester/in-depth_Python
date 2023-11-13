"""The 'strip_range' decorator takes three arguments in the following order:

start — non-negative integer
end — non-negative integer
char is a single character, defaulting to dot.

The decorator modifies the return value of the function being
decorated by replacing all characters in the index range from
start (inclusive) to end (not inclusive) with a char character.

The decorator also stores the name and docstring of the function being decorated."""

from functools import wraps


def strip_range(start: int, end: int, char: str = '.'):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if end <= len(value):
                return value.replace(value[start:end], char * len(value[start:end]), 1)
            return value.replace(value[start:len(value)], char * len(value[start:end]), 1)

        return wrapper

    return decorator


@strip_range(3, 20, '_')
def beegeek():
    return 'beegeek'


print(beegeek())

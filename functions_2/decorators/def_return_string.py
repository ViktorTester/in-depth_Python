"""The returns_string decorator checks that the return value of the function
being decorated is of type str. If the return value is of some other type,
the decorator raises a TypeError exception."""

from functools import wraps


def returns_string(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, str):
            raise TypeError
        return result

    return wrapper

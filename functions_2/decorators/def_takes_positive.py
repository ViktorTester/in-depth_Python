"""The 'takes_positive' decorator checks that all arguments passed
to the function being decorated are positive integers."""

from functools import wraps


def takes_positive(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("Arguments should be integers.")
            if arg <= 0:
                raise ValueError("Arguments should be positive integers.")

        for value in kwargs.values():
            if not isinstance(value, int):
                raise TypeError("Keyword arguments should be integers.")
            if value <= 0:
                raise ValueError("Keyword arguments should be positive integers.")

        return func(*args, **kwargs)

    return wrapper

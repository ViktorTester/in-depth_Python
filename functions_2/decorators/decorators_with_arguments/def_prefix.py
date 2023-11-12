"""The prefix decorator takes two arguments in the following order:

string — arbitrary string
to_the_end - boolean value, defaults to False

The decorator adds string to the return value of the function being decorated.
If to_the_end is True, string is added to the end; if False, it is added to the beginning.

The decorator also stores the name and docstring of the function being decorated."""

from functools import wraps


def prefix(string: str, to_the_end=False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not to_the_end:
                return string + func(*args, **kwargs)
            return func(*args, **kwargs) + string

        return wrapper

    return decorator

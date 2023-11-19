"""The 'retry' decorator takes one argument:

times — natural number

The decorator retries the function it is decorating if an error occurs
during its execution. The decorator calls this until it runs out of times,
at which point it throws a MaxRetriesException.

The decorator also stores the name and docstring of the function being decorated."""

from functools import wraps


class MaxRetriesException(Exception):
    pass


def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == times - 1:
                        raise MaxRetriesException from e

        return wrapper

    return decorator

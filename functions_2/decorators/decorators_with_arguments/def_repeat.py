"""The 'repeat' decorator takes one argument:

times — natural number

The decorator calls the decorated function times times.

The decorator also stores the name and docstring of the function being decorated."""

from functools import wraps


def repeat(times=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, times + 1):
                value = func(*args, **kwargs)
            return value

        return wrapper

    return decorator


@repeat(4)
def say_beegeek():
    '''documentation'''
    print('beegeek')


print(say_beegeek.__name__)
print(say_beegeek.__doc__)

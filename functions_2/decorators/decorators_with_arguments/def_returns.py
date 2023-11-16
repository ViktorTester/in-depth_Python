"""The 'returns' decorator takes one argument:

'datatype' - data type

The decorator checks that the return value of the function being decorated
is of datatype. If the return value is of some other type,
the decorator throws a TypeError exception.

The decorator also stores the name and docstring of the function being decorated."""

from functools import wraps


def returns(datatype):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            if not isinstance(value, datatype):
                raise TypeError
            return value

        return wrapper

    return decorator


@returns(int)
def add(a, b):
    return a + b


try:
    print(add('199', '1'))
except TypeError as e:
    print(type(e))

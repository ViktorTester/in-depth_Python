"""The 'takes' decorator takes an arbitrary number of
positional arguments, each of which is a data type.

The decorator checks that the arguments passed to the
function being decorated are one of these types. If at least
one argument does not belong to one of these types,
the decorator raises a TypeError exception.

The decorator also stores the name and docstring
of the function being decorated."""

from functools import wraps


def takes(*types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            all_args = args + tuple(kwargs.values())
            for i in all_args:
                counter = 0
                for j in types:
                    if not isinstance(i, j):
                        counter += 1
                if counter == len(types):
                    raise TypeError
            return func(*args, **kwargs)

        return wrapper

    return decorator


@takes(str)
def beegeek(word, repeat):
    return word * repeat


try:
    print(beegeek('beegeek', repeat=2))
except TypeError as e:
    print(type(e))


@takes(list, bool, float, int)
def repeat_string(string, times):
    return string * times


try:
    print(repeat_string('bee', 4))
except TypeError as e:
    print(type(e))
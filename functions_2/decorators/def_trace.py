"""The 'trace' decorator displays debugging information about the
function being decorated as it runs, such as the function name,
the arguments passed, and the return value."""

from functools import wraps


def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'TRACE: call {func.__name__}() with arguments: {args}, {kwargs}')
        print(f"TRACE: return value {func.__name__}(): {repr(result)}")
        return func(*args, **kwargs)

    return wrapper


@trace
def func(nums):
    '''great feature'''
    return list(i ** 2 for i in nums)


print(func.__name__)
print(func.__doc__)
func([1, 2, 3, 4, 5, 6])

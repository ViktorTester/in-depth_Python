"""The 'ignore_exception' decorator takes an arbitrary number
of positional arguments - exception types, and displays the text:

Exception <exception type> handled

if during execution of the decorated function an exception
belonging to one of the passed types was raised.

If the exception raised is not one of the passed types, it is raised again."""

from functools import wraps


def ignore_exception(*exception_types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_types as e:
                print(f"Exception {type(e).__name__} handled")
            except Exception as e:
                raise e

        return wrapper

    return decorator


@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def f(x):
    return 1 / x


f(0)

"""The reverse_args decorator passes all positional arguments
to the func function being decorated in reverse order."""


def reverse_args(func):
    def wrapper(*args, **kwargs):
        rev = list(reversed(args))
        result = func(*rev, **kwargs)
        return result

    return wrapper


@reverse_args
def operation(a, b, name):
    return a // b + name


print(operation(10, 90, name=1))

"""The program, using a decorator, overrides the print()
function so that it prints all text in uppercase."""


def uppercase_print(func):
    def wrapper(*args, sep=' ', end='\n'):
        args = [str(arg).upper() for arg in args]
        func(*args, sep=sep.upper(), end=end.upper())

    return wrapper


print = uppercase_print(print)

print('hi', 'there', end='xxx')

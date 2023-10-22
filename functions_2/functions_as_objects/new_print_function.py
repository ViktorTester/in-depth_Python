"""The program overrides the built-in print() function so that
it prints all string arguments passed in uppercase.

The values sep and end are also converted to upper case."""

output = print


def print(*args, sep=' ', end='\n'):
    arr = [i.upper() if isinstance(i, str) else i for i in args]
    output(*arr, sep=sep.upper(), end=end.upper())

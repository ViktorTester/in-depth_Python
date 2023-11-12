"""The make_html() decorator takes one argument:

tag - HTML tag, for example del

The decorator wraps the return value of the function being decorated in an HTML tag 'tag'.

The decorator also stores the name and docstring of the function being decorated."""

from functools import wraps


def make_html(tag: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)}</{tag}>'

        return wrapper

    return decorator

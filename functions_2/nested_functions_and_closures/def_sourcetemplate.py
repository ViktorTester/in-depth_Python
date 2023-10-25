"""Query string is the part of the URL containing the keys and their values.
It starts after the question mark and goes to the end of the address.

The sourcetemplate() function takes one argument:

url - URL address

The sourcetemplate() function returns a function that takes an arbitrary
number of named arguments and returns a URL combined with a query string
formed from the arguments passed. When called without arguments,
it returns the original url without changes.

Parameters in the query string are arranged in lexicographic order of the keys."""


def sourcetemplate(url: str):
    def func(**kwargs) -> str:
        if len(kwargs) > 0:
            new_url = url + '?'
            counter = 1
            for key, value in sorted(kwargs.items()):
                if counter != len(kwargs):
                    new_url += f"{key}={value}&"
                    counter += 1
                else:
                    new_url += f"{key}={value}"
            return new_url
        return url

    return func

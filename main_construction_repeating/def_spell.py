"""The spell() function takes an arbitrary number of
positional word arguments and returns a dictionary
whose keys are the first letters of the words and whose
values are the maximum word lengths starting with that letter."""


def spell(*args: str) -> dict:
    d = {}
    for i in args:
        if i[0].lower() not in d:
            d[i[0].lower()] = len(i)
        else:
            for key, value in d.items():
                if i[0].lower() == key and len(i.lower()) > value:
                    d[key] = len(i.lower())

    return d

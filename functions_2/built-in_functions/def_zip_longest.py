"""The zip_longest() function takes a variable number of positional arguments,
each of which is a list, and one optional named argument fill, which defaults to None.

The function combines the elements of the passed sequences into tuples,
similar to the zip() function, and returns it as a list, but if the sequences
have different lengths, the missing elements of the shorter sequences take the value fill."""


def zip_longest(*args, fill=None):
    max_length = max(map(len, args))
    arr = []
    for i in range(max_length):
        temp = []
        for arg in args:
            if i < len(arg):
                temp.append(arg[i])
            else:
                temp.append(fill)
        arr.append(tuple(temp))
    return arr

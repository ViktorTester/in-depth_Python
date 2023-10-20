"""The hash_as_key() function takes one argument:

objects — list of hashable objects

The function returns a dictionary whose key is the hash value of an object from
the objects list, and the value is the object itself. If the hash values of
some objects match, the function combines them into a list."""


def hash_as_key(objects):
    d = {}
    for i in objects:
        i_hash = hash(i)
        if i_hash in d:
            if isinstance(d[i_hash], list):
                d[i_hash].append(i)
            else:
                d[i_hash] = [d[i_hash], i]
        else:
            d[i_hash] = i
    return d

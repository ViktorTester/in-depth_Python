"""There is a 'people.json' file containing a list of JSON objects.
Moreover, different objects can have a different number of keys.

The program adds to each JSON object from the given list all
the missing keys, setting these keys to null. A key is considered
missing if it is present in some other object but absent in this one."""

import json

with open('people.json', encoding='utf-8') as file1:
    data1 = list(json.load(file1))

    longest = max(data1, key=len)

    for i in data1:
        for key, value in longest.items():
            if key not in i:
                i[key] = i.get(key, None)

with open('updated_people.json', 'w') as end:
    json.dump(data1, end)

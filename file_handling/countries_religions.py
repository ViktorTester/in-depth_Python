"""There is a file countries.json containing a list of JSON objects
with information about countries and religions practiced in them.

The program creates a single JSON object with the name of the religion
as the key and a list of countries where
the religion is practiced as the value."""

import json

with open('countries.json', encoding='utf-8') as file1:
    data1 = json.load(file1)

    d = {}

    for entry in data1:
        religion = entry.get('religion', None)
        country = entry.get('country', None)

        if religion is not None and country is not None:
            if religion not in d:
                d[religion] = [country]
            else:
                d[religion].append(country)

with open('religion.json', 'w') as end:
    json.dump(d, end)

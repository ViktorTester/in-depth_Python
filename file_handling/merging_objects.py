"""There are two files э and э,
each containing a single JSON object.

The program merges two given JSON objects into one JSON object,
and if pairs from the first and second objects have matching keys,
then the value is taken from the second object."""

import json

with (open('data1.json', encoding='utf-8') as file1,
      open('data2.json', encoding='utf-8') as file2):

    data1 = json.load(file1)
    data2 = json.load(file2)

    data1.update(data2)

with open('data_merge.json', 'w') as end:
    json.dump(data1, end)

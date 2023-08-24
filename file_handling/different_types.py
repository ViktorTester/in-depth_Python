"""There is a data.json file containing a list of various objects.

The program creates a list whose elements are objects from the list
contained in the data.json file, modified according to the following rules:

if the object is a string, an exclamation mark is added to the end
if the object is a number, it increments by one
if the object is a boolean, it is inverted
if the object is a list, it doubles
if the object is a JSON object (dictionary), a new "newkey": null pair is added to it
if the object is an empty value (null), it is not added"""

import json

with open('data.json', encoding='utf-8') as file:
    data = json.load(file)
    arr = []

    for i in data:
        if isinstance(i, str):
            arr.append(i + '!')
        elif isinstance(i, bool):
            arr.append(not i)
        elif isinstance(i, (int, float, complex)):
            arr.append(i + 1)
        elif isinstance(i, list):
            arr.append(i * 2)
        elif isinstance(i, dict):
            i.update({"newkey": None})
            arr.append(i)
        elif i is None:
            continue

with open('updated_data.json', 'w') as file2:
    json.dump(arr, file2)

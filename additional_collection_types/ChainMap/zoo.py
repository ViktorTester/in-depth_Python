"""There is a file zoo.json containing a list of JSON objects with data about the
inhabitants of a certain zoo. The key in each object is the name of the animal,
the value is the number of animals in the zoo.

The program determines how many animals live in the zoo and displays the result."""

from collections import ChainMap
import json

with open('zoo.json', encoding='utf-8') as file:
    data = json.load(file)

    total = 0

    for value in ChainMap(*data).values():
        total += value

    print(total)

"""The program takes as input a description of one object in
JSON format and outputs all key-value pairs of this object."""

import json
import sys

data = json.load(sys.stdin)

for key, value in data.items():
    if not isinstance(value, list):
        print(f'{key}: {value}')
    else:
        print(f'{key}: {", ".join(map(str, value))}')

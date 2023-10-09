"""The program takes the name of a JSON file as input, deserializes
the object contained in this file and outputs it.

if a file with this name is not in the program folder, the program displays the text:
File not found

if a file with this name contains incorrect data
(that is, not satisfying the JSON format), the program displays the text:
Error during deserialization"""

import json

name = input()

try:
    with open(f'{name}', encoding='utf-8') as file:
        text = json.load(file)
        print(text)
except FileNotFoundError:
    print('File not found')
except json.decoder.JSONDecodeError:
    print('Error during deserialization')

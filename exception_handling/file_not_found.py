"""The program takes as input the name of a text file and displays its contents."""

name = input()

try:
    with open(f'{name}', encoding='utf-8') as file:
        text = file.read()
        print(text)
except FileNotFoundError:
    print('File not found')

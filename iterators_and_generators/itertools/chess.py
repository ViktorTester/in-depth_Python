"""The program displays all symbols of the fields of the
chess board in alphabetical order through a space."""

from string import ascii_lowercase
from itertools import product

letters = ascii_lowercase[:8]
digits = [1, 2, 3, 4, 5, 6, 7, 8]

for i in list(product(letters, digits)):
    print(*i, sep='', end=' ')

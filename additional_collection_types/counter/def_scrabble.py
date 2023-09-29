"""The scrabble() function takes two arguments in the following order:

symbols — set of symbols
word - word

The function returns True if the word 'word' can be formed
from the set of symbols, or False otherwise."""

from collections import Counter


def scrabble(symbols: str, word: str) -> bool:
    x = Counter(symbols.lower())
    y = Counter(word.lower())
    total = 0

    for key, value in y.items():
        for k, v in x.items():
            if key == k and value <= v:
                total += 1

    if total == len(y):
        return True
    return False


# or:

def scrabble(symbols, word):
    return Counter(word.lower()) <= Counter(symbols.lower())

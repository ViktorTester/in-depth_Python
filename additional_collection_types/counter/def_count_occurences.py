"""The count_occurences() function takes two arguments in the following order:

word - word
words — a sequence of words separated by a space

The function determines how many times the word 'word'
appears in the sequence words and returns the result."""

from collections import Counter


def count_occurences(word: str, words: str) -> int:
    counter = Counter((words.lower()).split())
    return counter[word.lower()]

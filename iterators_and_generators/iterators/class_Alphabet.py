"""The 'Alphabet' class generates iterators, its constructor takes one argument:

language — language code: ru — Russian, en — English

The Alphabet() class iterator cyclically generates a sequence of lowercase letters:

Russian alphabet, if language is 'ru'
English alphabet if language is 'en'

The letter 'ё' is not taken into account in the Russian alphabet."""

from itertools import cycle


class Alphabet:
    def __init__(self, language):
        if language == 'ru':
            self.alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        elif language == 'en':
            self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        else:
            raise ValueError("Unsupported language")

        self.cycle_alphabet = cycle(self.alphabet)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.cycle_alphabet)


en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)

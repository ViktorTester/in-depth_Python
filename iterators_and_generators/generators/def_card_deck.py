"""The card_deck() generator function takes one argument:

suit - one of four card suits: spades, clubs, diamonds, hearts

The function returns a generator that cyclically generates a deck of playing cards without 'suit'."""


def card_deck(suit):
    nominals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', ' king', 'ace']
    suits = ['spade', 'clubs', 'diamond', 'hearts']

    while True:
        for s in suits:
            if s != suit:
                for nominal in nominals:
                    yield f'{nominal} {s}'


generator = card_deck('spade')
cards = [next(generator) for _ in range(40)]

print(*cards)

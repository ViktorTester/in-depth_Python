'''The 'CardDeck' class generates iterators;
its constructor does not take any arguments.

The 'CardDeck class' iterator generates a sequence of
52 playing cards and then raises a StopIteration exception.'''
class CardDeck:
    def __init__(self):
        self.suits = ['spade', 'clubs', 'diamond', 'hearts']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', ' king', 'ace']
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 52:
            suit_index = self.index // 13
            rank_index = self.index % 13
            card = f"{self.ranks[rank_index]} {self.suits[suit_index]}"
            self.index += 1
            return card
        else:
            raise StopIteration


cards = list(CardDeck())

print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])
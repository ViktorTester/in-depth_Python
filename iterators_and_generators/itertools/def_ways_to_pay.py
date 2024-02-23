"""A boy came to a bookstore to buy a new book that cost $100. He has many bills
of various denominations in his wallet, which are presented in the wallet list.
For example, he can pay with one $100 bill or two $50 bills.

The program displays the number of ways a boy can purchase a book worth $100."""

from itertools import combinations


def count_ways_to_pay(amount, wallet):
    ways = set()

    for r in range(1, len(wallet) + 1):
        for i in combinations(wallet, r):
            if sum(i) == amount:
                ways.add(tuple(sorted(i)))

    return len(ways)


# Пример использования
wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
amount = 100

ways = count_ways_to_pay(amount, wallet)
print(ways)

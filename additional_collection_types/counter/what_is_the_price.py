"""Let's say the price of a product is determined as the sum of the Unicode
codes of the letters of its name. The letter designation of this currency
is two capital Latin letters UC. For example, an apple costs:

1088 + 1091 + 1095 + 1082 + 1072 = 5428 UC

The boy is making a shopping list, but since the number block on his keyboard
has stopped working, instead of indicating the quantity of an item by number,
he adds it to the ssdhopping list as many times as he plans to buy.

The program groups identical products from a given
shopping list and determines the cost of each group."""

from collections import Counter

s = input().split(',')

top_len = len(max(s, key=len))

s = Counter(s)

for key, value in sorted(s.items()):
    total = 0
    for i in key:
        if i.isalnum():
            total += ord(i)
    print(f'{key.ljust(top_len)}: {total} UC x {value} = {total * value} UC')

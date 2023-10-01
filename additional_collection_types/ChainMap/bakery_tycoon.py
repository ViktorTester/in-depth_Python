"""The price of each burger in a restaurant is determined by the number
of ingredients that the visitor chooses. There are dictionaries in which
the name of the ingredient is indicated as the key, and its price as the value.
All ingredients are divided into categories, for example,
vegetables are contained in one dictionary, sauces in another.

The program accepts the ingredients selected by the
visitor as input and determines their total cost.

The input to the program is a sequence of ingredients
separated by a comma without spaces."""

from collections import ChainMap, Counter

bread = {'sesame bun': 15, 'regular bun': 10, 'rye bun': 15}
meat = {'chicken steak': 50, 'beef steak': 70, 'fish steak': 40}
sauce = {'creamy garlic': 15, 'ketchup': 10, 'mustard': 10, 'barbecue': 15, 'chili': 15}
vegetables = {'onion': 10, 'salad': 15, 'tomato': 15, 'cucumbers': 10}
toppings = {'cheese': 25, 'egg': 15, 'bacon': 30}

s = Counter(input().split(','))
top_len = len(max(s, key=len))

all_food = ChainMap(bread, meat, sauce, vegetables, toppings)

total = 0
d = {}
arr = []

for key1, value1 in all_food.items():
    for key2, value2 in s.items():
        if key1 == key2 and value2 <= value1:
            total += value2 * value1

for key, value in sorted(s.items()):
    arr.append(f'{key.ljust(top_len)} x {value}')
arr.append(f'TOTAL: {total // 100}.{total % 100}$')

for i in arr[:-1]:
    print(i)
print(len(max(arr, key=len)) * '-')
print(arr[-1])

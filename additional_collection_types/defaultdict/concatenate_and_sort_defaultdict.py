"""There is a 'data' list of tuples with data on the income of some
educational resource. The first element of the tuple is the
product name, the second is the profit in dollars.

The program determines how much total income each product brought
in and displays the names of all products, indicating the corresponding
total profit for each. The products are arranged
in lexicographical order, each on a separate line."""

from collections import defaultdict

data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061),
        ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041),
        ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729),
        ('Tutorials', 977), ('Books', 656)]

ddict = defaultdict(int)

for i, j in data:
    ddict[i] += j

for key, value in sorted(ddict.items()):
    print(f'{key}: ${value}')

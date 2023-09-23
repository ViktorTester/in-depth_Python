"""There is a dictionary data with an even number of elements.
The program displays this dictionary, arranging its elements according
to the following rule: first, last, second, second to last, third, and so on."""

from collections import OrderedDict

data = OrderedDict({'Name': 'apple', 'IsNetObject': 'yes', 'OperatingCompany': 'apple', 'TypeObject': 'pub',
                    'AdmArea': 'London', 'District': 'Baker street',
                    'Address': 'Baker street 222b', 'SeatsCount': '10'})

arr = []
data2 = data.copy()

for i in range(1, len(data) + 1):
    if i % 2 == 1:
        arr.append(data2.popitem(last=False))
    else:
        arr.append(data2.popitem())

print(OrderedDict(arr))

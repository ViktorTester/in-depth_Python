"""There is a dictionary data. The program displays this dictionary,
arranging its elements in reverse order."""

from collections import OrderedDict

data = OrderedDict({'Name': 'apple', 'IsNetObject': 'yes', 'OperatingCompany': 'apple', 'TypeObject': 'pub',
                    'AdmArea': 'London', 'District': 'Baker street',
                    'Address': 'Baker street 222b', 'SeatsCount': '10'})

arr = [data.popitem() for _ in range(len(data))]

print(OrderedDict(arr))

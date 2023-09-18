"""There is a named tuple Animal that contains data about the animal.
The first element of the named tuple is the name of the animal,
the second is the family, the third is the gender, and the fourth is the color.
A data.pkl file containing a serialized list of such tuples is also available.

The program, for each tuple from this list,
displays the names of its fields and the values of these fields."""

from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as file:
    obj = pickle.load(file)

    for j in obj:
        for fields, values in zip(j._fields, j):
            print(fields + ':', values)
        print()

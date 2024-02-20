"""There is a named tuple 'Person' that contains data about a person.
The first element of the named tuple is the person's name, the second is age,
and the third is height. A list of persons containing these tuples is also available.

The program groups people from this list by their height and displays the resulting groups.
For each group, height is first indicated, and then the names of people with the corresponding
height are listed, separated by commas. The groups are arranged in order
of increasing height, each on a separate line, the names in the groups
are in alphabetical order, in the following format:

<height>: <name>, <name>, ..."""

from collections import namedtuple
from itertools import groupby

Person = namedtuple('Person', ['name', 'age', 'height'])

persons = [Person('Tim', 63, 193), Person('Eva', 47, 158),
           Person('Mark', 71, 172), Person('Alex', 45, 193),
           Person('Jeff', 63, 193), Person('Ryan', 41, 184),
           Person('Ariana', 28, 158), Person('Liam', 69, 193)]

persons.sort(key=lambda x: x.height)

grouped_persons = groupby(persons, key=lambda x: x.height)

for height, group in grouped_persons:
    names = ', '.join(sorted(person.name for person in group))
    print(f"{height}: {names}")

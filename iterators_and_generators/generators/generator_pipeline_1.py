"""The named 'Person' tuple contains data about a person. The first element of the
named tuple is the person’s first and last name, the second is nationality,
the third is gender, the fourth is the year of birth, the fifth is the year of death.
If the person is alive, the year of death is considered to be 0.
A  'persons' list containing these tuples is also available.

The program, using generator pipelines, outputs the first and
last name of the youngest living male from Sweden."""

from collections import namedtuple

Person = namedtuple('Person', ['name', 'nationality', 'sex', 'birth', 'death'])

persons = [Person('E. M. Ashe', 'American', 'male', 1867, 1941),
           Person('Goran Aslin', 'Swedish', 'male', 1980, 0),
           Person('Erik Gunnar Asplund', 'Swedish', 'male', 1885, 1940),
           Person('Genevieve Asse', 'French', 'female', 1949, 0),
           Person('Irene Adler', 'Swedish', 'female', 2005, 0),
           Person('Sergio Asti', 'Italian', 'male', 1926, 0),
           Person('Olof Backman', 'Swedish', 'male', 1999, 0),
           Person('Alyson Hannigan', 'Swedish', 'female', 1940, 1987),
           Person('Dana Atchley', 'American', 'female', 1941, 2000),
           Person('Monika Andersson', 'Swedish', 'female', 1957, 0),
           Person('Shura_Stone', 'Russian', 'male', 2000, 0),
           Person('Jon Bale', 'Swedish', 'male', 2000, 0)]


def age(data):
    for i in data:
        if i[2] == 'male':
            yield i


def nationality(data):
    for i in data:
        if i[1] == 'Swedish':
            yield i


def dead(data):
    for i in data:
        if i[4] == 0:
            yield i


def youngest(data):
    max_age = 0
    for i in data:
        if i[3] > max_age:
            max_age = i[3]
    if i[3] == max_age:
        yield i


for j in list(youngest(dead(nationality(age(persons))))):
    print(j[0])

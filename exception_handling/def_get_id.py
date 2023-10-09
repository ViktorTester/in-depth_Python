"""A student's name is considered correct if it begins with a capital
Latin letter followed by lowercase Latin letters. Each student also has an
identification number, represented by a natural number. For example,
if there are 10 students in a school, then a new arriving student
will receive an identification number of 11.

The get_id() function takes two arguments:

'names' - list of names of students studying at the school
'name' — name of the incoming student

The function returns the identification number that
the student entering the school will receive, while

if the student name is not a string (type str),
the function raises an exception: TypeError('Name is not a string')

if student name is a string (type str) but is not a valid name,
raises an exception: ValueError('Name is not valid')"""


def get_id(names: list, name: str) -> int:
    if not isinstance(name, str):
        raise TypeError('Name is not a string')
    if name != name.capitalize() or not name.isalpha():
        raise ValueError('Name is not valid')
    return len(names) + 1

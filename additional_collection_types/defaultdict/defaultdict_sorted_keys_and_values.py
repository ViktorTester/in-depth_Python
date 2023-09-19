"""There is a 'staff_broken' list of tuples with data about employees of a certain company.
The first element of the tuple is the name of the department, the second is the first
and last name of the employee working in this department.
Some employees may appear on the list more than once.

The program groups employees into the appropriate departments and displays the names
of all departments, indicating for each the first and last names of its employees.
Departments, as well as the first and last names of employees in these departments,
are arranged in lexicographic order, each on a separate line"""

from collections import defaultdict

staff_broken = [('Developing', 'Miguel Norris'), ('Sales', 'Connie Reid'), ('Sales', 'Joseph Lee'),
                ('Marketing', 'Carol Peters'), ('Accounting', 'Linda Hudson'), ('Accounting', 'Ann Bell'),
                ('Marketing', 'Ralph Morgan'), ('Accounting', 'Gloria Higgins'), ('Developing', 'Wilma Woods'),
                ('Developing', 'Wilma Woods'), ('Marketing', 'Bernice Ramos'), ('Marketing', 'Joyce Lawrence'),
                ('Accounting', 'Craig Wood'), ('Developing', 'Nicole Watts'), ('Sales', 'Jose Taylor'),
                ('Accounting', 'Linda Hudson'), ('Accounting', 'Edna Cunningham'), ('Sales', 'Jose Taylor'),
                ('Marketing', 'Helen Taylor'), ('Accounting', 'Kimberly Reynolds'), ('Marketing', 'Mary King'),
                ('Sales', 'Joseph Lee'), ('Accounting', 'Gloria Higgins'), ('Marketing', 'Andrew Clark'),
                ('Accounting', 'John Watts'), ('Accounting', 'Rosemary Garcia'), ('Accounting', 'Steven Diaz'),
                ('Marketing', 'Mary King'), ('Sales', 'Gladys Taylor'), ('Developing', 'Thomas Porter'),
                ('Accounting', 'Brenda Davis'), ('Sales', 'Connie Reid'), ('Sales', 'Alicia Mendoza'),
                ('Marketing', 'Mario Reynolds'), ('Sales', 'John White'), ('Developing', 'Joyce Rivera'),
                ('Accounting', 'Steven Diaz'), ('Developing', 'Arlene Gibson'), ('Sales', 'Robert Barnes'),
                ('Sales', 'Charlotte Cox'), ('Accounting', 'Craig Wood'), ('Marketing', 'Carol Peters'),
                ('Marketing', 'Ralph Morgan'), ('Accounting', 'Kay Scott'), ('Sales', 'Evelyn Martin'),
                ('Marketing', 'Billy Lloyd'), ('Sales', 'Gladys Taylor'), ('Developing', 'Deborah George'),
                ('Sales', 'Charlotte Cox'), ('Marketing', 'Sam Davis'), ('Sales', 'John White'),
                ('Sales', 'Marie Cooper'), ('Marketing', 'John Gonzalez'), ('Sales', 'John Washington'),
                ('Sales', 'Chester Fernandez'), ('Sales', 'Alicia Mendoza'), ('Sales', 'Katie Warner'),
                ('Accounting', 'Jane Jackson'), ('Sales', 'Chester Fernandez'), ('Marketing', 'Charles Bailey'),
                ('Marketing', 'Gail Hill'), ('Accounting', 'Casey Jenkins'), ('Accounting', 'James Wilkins'),
                ('Accounting', 'Casey Jenkins'), ('Marketing', 'Mario Reynolds'), ('Accounting', 'Aaron Ferguson'),
                ('Accounting', 'Kimberly Reynolds'), ('Sales', 'Robert Barnes'), ('Accounting', 'Aaron Ferguson'),
                ('Accounting', 'Jane Jackson'), ('Developing', 'Deborah George'), ('Accounting', 'Michelle Wright'),
                ('Accounting', 'Dale Houston')]

ddict = defaultdict(str)

for i, j in staff_broken:
    if j not in ddict[i]:
        ddict[i] += f'{j}, '

for key, value in ddict.items():
    names_list = value.split(', ')
    sorted_names = ', '.join(sorted(names_list))
    ddict[key] = sorted_names[2:]

for key, value in sorted(ddict.items()):
    print(f'{key}: {value}')

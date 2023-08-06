"""There is a salary_data.csv file that contains anonymous
information about the salaries of employees in various companies.
The first column contains the name of the company,
and the second column contains the salary of the next employee.

The program sorts companies in ascending order of the average
salary of their employees and displays their names, each on a
separate line. If two companies have the same average salary,
then they are listed in the lexicographic order of their names."""

import csv

with open('salary_data.csv', encoding='utf-8') as file:
    rows = csv.DictReader(file, delimiter=';')
    d = {}
    for row in rows:
        if row['company_name'] not in d:
            d[row['company_name']] = []
        d[row['company_name']].append(int(row['salary']))

    for key, value in d.items():
        average_salary = sum(value) / len(value) if len(value) > 0 else 0
        d[key] = average_salary

    for key, value in sorted(d.items(), key=lambda x: (x[1], x[0])):
        print(key)

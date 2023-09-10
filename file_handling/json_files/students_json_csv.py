"""I have a 'students.json' file that contains a list of JSON
objects that represent student data for a course.

"Student" means one JSON object from this list.
The student has the following attributes:

name - name
city — city of residence
age - age
progress — progress on the rate in percent
phone— contact number

The program determines students who meet the following conditions:

age 18 or over
course progress of 75% or more

The program creates a 'data.csv' file with two columns - name (name)
and phone (number), and writes the data of the selected students
into it, arranging them in the lexicographic order of names."""

import json
import csv

with open('students.json', encoding='utf-8') as file1:
    rows = json.load(file1)

    result = []

    for row in rows:
        if row['age'] >= 18 and row['progress'] >= 75:
            result.append([row['name'], row['phone']])
    result.sort()

with open('data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['name', 'phone'])
    writer.writerows(result)

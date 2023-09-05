"""There is a student_counts.csv file that contains data on the number
of students in a certain educational institution for the period 2000 - 2021.
The first column contains the year, the subsequent columns contain the
class and the number of students in this class this year.

The program writes this table to the file sorted_student_counts.csv,
arranging all columns in ascending order of classes,
if classes match, in ascending order of letters."""

import csv

with open('student_counts.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file))
    columns = sorted(reader[0])

    arr = [i.split('-') for i in columns[:-1]]

    new_columns = sorted(arr, key=lambda x: int(x[0]))

    for i in range(len(columns)):
        new_columns[i] = '-'.join(new_columns[i])

    new_columns.insert(0, 'year')

with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=new_columns, delimiter=',')
    writer.writeheader()
    writer.writerows(reader)

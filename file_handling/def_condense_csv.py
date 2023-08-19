"""The condense_csv() function takes two arguments in the following format:

filename - name of the csv file, for example, data.csv; the format of the
file content is similar to the format of the text fragment considered in
the problem condition: each line of the file contains three values
separated by commas, namely the name of the object, the property of this
object, the value of the property; all objects
have equal properties and in equal quantities

id_name - common name for objects

The function converts the contents of the file into the usual CSV format by
grouping the rows by the first column and naming the first column id_name.
The function writes the result to the condensed.csv file."""

import csv


def condense_csv(filename, id_name):
    data_dict = {}

    with open(filename, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)

        for row in csv_reader:
            object_name, property_name, property_value = row
            if object_name not in data_dict:
                data_dict[object_name] = {}
            data_dict[object_name][property_name] = property_value

    with open('condensed.csv', mode='w', encoding='utf-8', newline='') as output_file:
        csv_writer = csv.writer(output_file)

        header = [id_name] + list(data_dict[next(iter(data_dict))].keys())
        csv_writer.writerow(header)

        for object_name, properties in data_dict.items():
            row = [object_name] + [properties[key] for key in header[1:]]
            csv_writer.writerow(row)

"""There is a text file 'diary.txt', which contains small reports for the day.
Each new report is written either to the beginning of the file, or to the
middle, or to the end. All reports are separated by an empty line.
Each new report starts with a line with a date and time in the format
DD.MM.YYYY; HH:MM followed by events that occurred on the specified day.

The program arranges all entries in chronological order and displays the result."""

from datetime import datetime

with open('diary.txt', encoding='utf-8') as file:
    text = [line.strip() if line.endswith('\n') else line + '\n' for line in file.readlines()]

    d = {}
    for i in text:
        if i[:2].isdigit():
            key = datetime.strptime(i[:10] + i[-6:], '%d.%m.%Y %H:%M')
            d[key] = []
        else:
            d[key].append(i)

    counter = 0
    for key, value in sorted(d.items()):
        first = key.strftime('%d.%m.%Y; %H:%M')
        print(first)
        counter += 1
        if counter != len(d):
            for y in value:
                print(y)
        else:
            for z in range(len(value) - 1):
                print(value[z])

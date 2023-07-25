"""A person performs tasks and adds the start and end times of
the task to the data list. Each result is a tuple, the first
element of which is the start time of the solution as a string
in the HH:MM format, the second element is the end time of the
solution as a string in the same format. The program displays
the total integer number of minutes spent on all tasks."""

from datetime import datetime, timedelta

data = [('07:14', '08:46'),
        ('09:01', '09:37'),
        ('10:00', '11:43'),
        ('12:13', '13:49'),
        ('15:00', '15:19'),
        ('15:58', '17:24'),
        ('17:57', '19:21'),
        ('19:30', '19:59')]

arr = []
for i in data:
    arr.append([datetime(2023, 1, 1, int(i[0][:2]), int(i[0][-2:])),
                datetime(2023, 1, 1, int(i[1][:2]), int(i[1][-2:]))])

result = datetime(2023, 1, 1)
for j in arr:
    result += j[1] - j[0]

delta = timedelta(hours=result.hour, minutes=result.minute, seconds=result.second)

print(int(delta.total_seconds() // 60))

"""The teacher conducts classes for 45 minutes with breaks of 10 minutes.
The teacher knows the start time of the working day and the end time of
the working day. The program generates and displays the class
schedule for the teacher for the whole working day."""

from datetime import datetime, timedelta

start = input().split(':')
end = input().split(':')
start_time = datetime(2023, 1, 1, int(start[0]), int(start[1]))
end_time = datetime(2023, 1, 1, int(end[0]), int(end[1]))

while end_time - timedelta(minutes=44) > start_time:
    arr = []
    arr.append(start_time.strftime('%H:%M') + ' -')
    start_time += timedelta(minutes=45)
    arr.append(start_time.strftime('%H:%M'))
    print(*arr)
    start_time += timedelta(minutes=10)

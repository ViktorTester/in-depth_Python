"""Two dates are given - the left and right boundaries of the range,
respectively. The program, from this range, including boundaries,
displays, starting from a date for which the sum of the day and
month is odd, every third date, only if it is not Monday or Thursday."""

from datetime import datetime, timedelta

start = day, month, year = map(int, input().split('.'))
start_date = datetime(year, month, day)
end = day, month, year = map(int, input().split('.'))
end_date = datetime(year, month, day)

arr = []
while start_date < end_date + timedelta(days=1):
    arr.append(start_date)
    start_date += timedelta(days=1)

counter, counter2 = 0, 0
for y, x in enumerate(arr):
    if (x.day + x.month) % 2 == 1:
        for j in arr[y:]:
            if counter != 1:
                counter = 1
                if j.isoweekday() not in (1, 4):
                    print(j.date().strftime('%d.%m.%Y'))
            else:
                counter2 += 1
                if j.isoweekday() not in (1, 4) and counter2 % 3 == 0:
                    print(j.date().strftime('%d.%m.%Y'))
        break

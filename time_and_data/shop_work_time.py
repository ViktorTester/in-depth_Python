"""The program takes the current date and time as input and
determines the number of minutes left before the store closes.

In 'd' dictionary, the store's work schedule is available."""

from datetime import datetime, timedelta

d = {1: [datetime(2023, 1, 1, 9), datetime(2023, 1, 1, 21)],
     2: [datetime(2023, 1, 1, 9), datetime(2023, 1, 1, 21)],
     3: [datetime(2023, 1, 1, 9), datetime(2023, 1, 1, 21)],
     4: [datetime(2023, 1, 1, 9), datetime(2023, 1, 1, 21)],
     5: [datetime(2023, 1, 1, 9), datetime(2023, 1, 1, 21)],
     6: [datetime(2023, 1, 1, 10), datetime(2023, 1, 1, 18)],
     7: [datetime(2023, 1, 1, 10), datetime(2023, 1, 1, 18)]}

s = input().split()

my_date = datetime(int(s[0][6:]), int(s[0][3:5]), int(s[0][:2]), int(s[1][:2]), int(s[1][3:]))

for key, value in d.items():
    if my_date.isoweekday() == key:
        if value[0].time() <= my_date.time() < value[1].time():
            answer = (timedelta(hours=value[1].hour, minutes=value[1].minute)
                      - timedelta(hours=my_date.hour, minutes=my_date.minute)).total_seconds() // 60
            print(int(answer))
        else:
            print('The store is closed')
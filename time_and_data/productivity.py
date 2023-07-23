"""The boy needs to do 10 household chores. So that the work does
not turn out to be tiring, he came up with a rule:

if today he did one thing, then he must do the second in one day
if today he did the second thing, then he must do the third in two days
if today he did the third thing, then he must do the fourth in three days
and so on

The program determines the dates in which Arthur needs to prepare the tasks."""

from datetime import timedelta, date

day, month, year = input().split('.')
my_date = date(int(year), int(month), int(day))
counter = 1

for i in range(10):
    print(my_date.strftime('%d.%m.%Y'))
    counter += 1
    my_date += timedelta(days=counter)

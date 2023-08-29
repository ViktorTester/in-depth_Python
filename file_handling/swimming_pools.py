"""The boy wants to go to the pool. Among all the pools,
those that are open on Monday from 10:00 to 12:00 are
suitable for him. He also likes to swim along long lanes,
so from all the pools operating at this time, you need to
choose the pool with the longest lane,
with equal values - with the largest width.

There is a pools.json file that contains a list of JSON
objects that represent data about indoor swimming pools.

The program determines the pool suitable for the boy."""

import json
from datetime import time

with open('pools.json', encoding='utf-8') as file1:
    rows = json.load(file1)

    needed_t_s = time(10, 0, )
    needed_t_e = time(12, 0, )
    arr = []

    for row in rows:
        times = row['WorkingHoursSummer']['Понедельник'].split('-')
        h_s = times[0].split(':')
        h_e = times[1].split(':')
        time_s = time(int(h_s[0]), int(h_s[1]))
        time_e = time(int(h_e[0]), int(h_e[1]))
        if time_s == needed_t_s and time_e >= needed_t_e:
            arr.append(row)

    for i in sorted(arr, key=lambda x: (x['DimensionsSummer']['Length'], x['DimensionsSummer']['Width']), reverse=True):
        print(f"{i['DimensionsSummer']['Length']}x{i['DimensionsSummer']['Width']}")
        print(i['Address'])
        break

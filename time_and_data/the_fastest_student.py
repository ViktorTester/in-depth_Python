"""There is a 'data' dictionary containing student results.
The key in the dictionary is the name of the student, and the
value is a tuple, the first element of which is the start time
of the solution, the second element is the end time of the solution.
The code prints out the name of the student who spent the least time on homework."""

from datetime import datetime

data = {'John': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'),
        'Jerry': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'),
        'Hanna': ('02.11.2021 04:41:54', '02.11.2021 05:39:40'),
        'April': ('02.11.2021 01:36:40', '02.11.2021 04:48:27'),
        'Mark': ('04.11.2021 07:51:19', '04.11.2021 09:53:53'),
        'Jessica': ('01.11.2021 11:26:06', '01.11.2021 12:56:24'),
        'Arnold': ('03.11.2021 11:09:41', '03.11.2021 14:37:41'),
        'Ben': ('03.11.2021 05:29:38', '03.11.2021 06:01:59'),
        'Kate': ('05.11.2021 13:05:03', '05.11.2021 14:27:41'),
        'Angie': ('03.11.2021 04:14:26', '03.11.2021 05:10:58'),
        'Naomi': ('05.11.2021 15:21:06', '05.11.2021 18:33:46')}

d = {key: tuple(map(lambda x: datetime.strptime(x, '%d.%m.%Y %H:%M:%S'), value)) for key, value in data.items()}
d2 = {key: value[1].timestamp() - value[0].timestamp() for key, value in d.items()}

fastest = 9999
leader = ''

for key, value in d2.items():
    if value < fastest:
        fastest = value
        leader = key

print(leader)
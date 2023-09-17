"""There is a named tuple User, which contains data about the user of some resource.
The first element of the named tuple is the user's name, the second is the last name,
the third is the email address, and the fourth is the subscription status.
A list of users containing these tuples is also available.

The program displays data about each user from this list, having previously
sorted it by subscription status from expensive to cheap, and if the
statuses match, in the lexicographical order of email addresses."""

from collections import namedtuple

User = namedtuple('User', ['name', 'surname', 'email', 'plan'])

users = [User('Mary', 'Griffin', 'sonnen@yahoo.com', 'Basic'),
         User('Brenda', 'Young', 'retoh@outlook.com', 'Silver'),
         User('Kathleen', 'Lyons', 'balchen@att.net', 'Gold'),
         User('Pamela', 'Hicks', 'corrada@sbcglobal.net', 'Silver'),
         User('William', 'Townsend', 'kosact@verizon.net', 'Gold'),
         User('Clayton', 'Morris', 'berserk@yahoo.com', 'Silver'),
         User('Dorothy', 'Dennis', 'sequin@live.com', 'Gold'),
         User('Tyler', 'Walker', 'noahb@comcast.net', 'Basic'),
         User('Joseph', 'Moore', 'ylchang@sbcglobal.net', 'Silver'),
         User('Kenneth', 'Richardson', 'tbusch@me.com', 'Bronze'),
         User('Stephanie', 'Bush', 'neuffer@live.com', 'Gold'),
         User('Gregory', 'Hughes', 'juliano@att.net', 'Basic'),
         User('Tracy', 'Wallace', 'sblack@me.com', 'Silver'),
         User('Russell', 'Smith', 'isaacson@comcast.net', 'Bronze'),
         User('Megan', 'Patterson', 'hoangle@outlook.com', 'Basic')]

plans = {'Gold': 1, 'Silver': 2, 'Bronze': 3, 'Basic': 4}

sorted_plans = sorted(users, key=lambda z: (plans[z.plan], z.email))

for user in users:
    print(f'{user.name} {user.surname}')
    print(f'  Email: {user.email}')
    print(f'  Plan: {user.plan}\n')

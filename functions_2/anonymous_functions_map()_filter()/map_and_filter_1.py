"""There is a 'data' list containing arbitrary objects.
The program displays all numbers (int and float types)
found in this list, discarding the fractional part of real numbers."""

data = ['Timur', -16.648911695768902, 'six', -202, 883.0093275936454, -765, (3, 4),
        -105.10718000213546, 976, -308.96857946288094, 458, ['one', 'two'],
        479.92207220345927, -87, -71, 'twelve', 112, -621, -715.0179551194733,
        'seven', 229, 729, -358, [1, 2, 3], -974, 882, -894.4709033242768, '',
        323.7720806756133, 'beegeek', -224, 431, 170.6353248658936, -343.0016746052049,
        'number', 104.17133679352878, [], -353.5964777099863, 'zero', -113, 288,
        None, -708.3036176571618]

filter1 = filter(lambda x: isinstance(x, (int, float)), data)

map1 = map(lambda y: str(y).split('.')[0], filter1)

for i in map1:
    print(i)

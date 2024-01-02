"""Let's say a range is a recording of two natural numbers separated by a hyphen a-b,
where 'a' is the left boundary of the range, 'b' is the right boundary of the range,
and a <= b. The range contains all numbers from 'a' to 'b' inclusive.

The parse_ranges() generator function takes one argument:

'ranges' - a string containing ranges of numbers separated by commas

The function returns a generator that generates a sequence of numbers contained in ranges."""


def parse_ranges(ranges: str):
    for i in ranges.split(','):
        i = i.split('-')
        counter = int(i[0])
        while counter != int(i[1]) + 1:
            yield int(counter)
            counter += 1

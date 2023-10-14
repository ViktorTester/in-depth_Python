"""In the first year, 77 frogs live in the pond. Every year, 30 frogs are caught
from the pond, and the remaining ones breed and become three times more numerous.

The number_of_frogs() function takes one argument:

year — natural number

The function returns a single number - the number of frogs in the pond in the year 'year'."""


def number_of_frogs(year: int) -> int:
    if year == 1:
        return 77
    return (number_of_frogs(year - 1) - 30) * 3

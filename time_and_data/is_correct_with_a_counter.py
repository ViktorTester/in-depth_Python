"""For each date entered, the program displays the text
Valid or Incorrect depending on whether the date is valid,
and then outputs the number of valid dates."""
from datetime import date

counter = 0


def is_correct(d: str, m: str, y: str) -> str:
    """The function returns True if the date is valid, False otherwise."""
    global counter
    try:
        date(int(y), int(m), int(d))
        counter += 1
        return 'Correct'
    except ValueError:
        return 'Incorrect'


while True:
    n = input().split('.')
    if n[0] == 'end':
        break
    day, month, year = n
    print(is_correct(day, month, year))

print(counter)
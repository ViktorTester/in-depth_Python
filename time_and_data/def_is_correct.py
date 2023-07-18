"""The function returns True if the date is valid, False otherwise."""
from datetime import date


def is_correct(day: int, month: int, year: int) -> bool:
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

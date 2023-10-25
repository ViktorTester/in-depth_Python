"""It is not uncommon for different countries to use different date formats.

The date_formatter() function takes one argument:

country_code — country code

The date_formatter() function returns a function that takes
a date (type date) as an argument and returns a string with
the given date in country format with country_code."""

from datetime import date

d = {'ru': '%d.%m.%Y',
     'us': '%m-%d-%Y',
     'ca': '%Y-%m-%d',
     'br': '%d/%m/%Y',
     'fr': '%d.%m.%Y',
     'pt': '%d-%m-%Y', }


def date_formatter(country_code: str):
    def func(td: date):
        for key, value in d.items():
            if country_code == key:
                return today.strftime(value)

    return func


date_ru = date_formatter('us')
today = date(2025, 1, 5)
print(date_ru(today))

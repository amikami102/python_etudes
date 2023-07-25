# date_detection.py
"""
A program that asks you to input a date in <day>/<month>/<year> format that
could plausibly exist after January 1st, 1990.

The program will print out whether the date is valid.

Usage example:
    $ python date_detection.py
    Type in any pluasible date after January 1st, 1990 in <day>/<month>/<year> format:
    30/10/92
    '30/10/92' is a valid date.
    
    $ python date_detction.py
    Type in any plausible date after January 1st, 1990 in <day>/<month>/<year> format:
    1/13/92
    '1/13/92' is not a valid date.
    
    $ python date_detection.py
    Type in any plausible date after January 1st, 1990 in <day>/<month>/<year> format:
    2023-09-21
    Your input, '2023-09-21', did not match the format.
"""
import re
from datetime import date
import pyperclip

DATE_RE = re.compile(
    r"""
    (\d{1,2})		# day
    /
    (\d{1,2})		# month
    /
    (\d{2,4})	# year
    """,
    re.VERBOSE
)


def is_valid_date(day: str, month: str, year: str) -> bool:
    """ Return True if a date  with `day`, `month`, and `year` values represents a valid date."""
    if len(year) == 2:
        year = f'20{year}' if year.startswith('0') else f'19{year}'
    try:
        date(int(year), int(month), int(day))
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    
    text = input('Type in any plausible date after January 1st, 1990 in <day>/<month>/<year> format:\n')
    
    if matched := DATE_RE.match(text):
        valid = is_valid_date(*matched.groups())
        if valid:
            print(f'{matched.group(0)!r} is a valid date.')
        else:
            print(f'{matched.group(0)!r} is not a valid date.')
    else:
        print(f'Your input, {text!r}, did not match the format.')
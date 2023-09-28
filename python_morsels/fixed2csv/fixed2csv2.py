# fixed2csv2.py
"""
A module for taking a fixed-width file and turning it into a csv file.
"""
from typing import *
from itertools import zip_longest
import re

COLUMN_RE = re.compile('.+?\s{2,}')


def get_column_slices(nonempty_row: str) -> Iterable[tuple[int, int]]:
    """Get the start and end indices of each column from `nonempty_row`."""
    slices = []
    start = 0
    for match in COLUMN_RE.finditer(nonempty_row):
        slices.append(
            (start, match.end())
        )
        start = match.end()
    slices.append((start, None))
    return slices
               

def parse_fixed_width_file(file: TextIO) -> Iterable[list[str]]:
    """Return an iterable of cell values as strings from each row in `file`."""
    slices = None
    for row in file:
        if slices is None:
            slices = get_column_slices(row)
            print(slices)
        yield [
            row[start:end].strip() if end else row[start:].strip()
            for (start, end) in slices
        ]
             


# base problem
from textwrap import dedent
from io import StringIO
expected = [
    ["2012", "Lexus"],
    ["2009", "GMC"],
    ["1965", "Ford"],
    ["2005", "Hyundai"],
    ["1995", "Mercedes-Benz"],
]
with open('two_columns.txt', 'r') as two_cols:
    assert list(parse_fixed_with_file(two_cols)) == expected
    #print(*list(parse_fixed_width_file(two_cols)), sep='\n')

expected = [
    ["2012", "Lexus", "LFA"],
    ["2009", "GMC", "Yukon XL 1500"],
    ["1965", "Ford", "Mustang"],
    ["2005", "Hyundai", "Sonata"],
    ["1995", "Mercedes-Benz", "C-Class"],
]
with open('cars.txt', 'r') as carsfile:
    assert list(parse_fixed_with_file(carsfile)) == expected
    #print(*list(parse_fixed_width_file(carsfile)), sep='\n')

# bonus 1, test with missing cell values
expected = [
    ["2012", "Lexus", "LFA"],
    ["", "Ford", "Mustang"],
    ["2005", "Hyundai", "Sonata"],
    ["1995", "Mercedes-Benz", ""],
]
with open('missing_values.txt', 'r') as missing:
    assert list(parse_fixed_width_file(missing)) == expected
    
# bonus 2, test with right-aligned content
expected = [
    ["23", "Breathe Owl Breathe", "~", "42"],
    ["14", "Three Dog Night", "It Ain't Easy", "2:51"],
    ["13", "Billy Joe Shaver", "Low Down Freedom", "2:53"],
    ["11", "Johnny Cash", "Folsom Prison Blues", "2:51"],
    ["4", "Kris Kristofferson", "To Beat The Devil", "4:05"],
    ["3", "Paul Simon", "Peace Like a River", "3:23"],
    ["2", "Waylon Jennings", "Honky Tonk Heroes (Like Me)", "3:29"],
]
with open('missing_values.txt', 'r') as missing:
    assert list(parse_fixed_width_file(missing)) == expected
    #print(*list(parse_fixed_width_file(missing)), sep='\n')
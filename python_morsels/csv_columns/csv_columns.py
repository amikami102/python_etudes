# csv_columns.py
"""
A script defining a function, `csv_columns()`, that returns a dictionary mapping CSV headers to column data.
"""
from typing import *
from itertools import zip_longest
import csv


def csv_columns(file: IO, *, headers: list[str] = None, missing: str = None) -> dict:
    """ Return dictionary mapping column data to their header entry. """
    reader = csv.reader(file)
    if not headers:
        headers = next(reader)
    return {
        head: data
        for head, *data in zip_longest(headers, *reader, fillvalue=missing)
    }


# base problem and bonus 1, test that the dictionary keys are in the same order as the csv header
assert csv_columns(open('my_file.csv')) ==\
       {'h1': ['1', '3'], 'h2': ['2', '4']}

# bonus 2, allow optional `headers` argument
assert csv_columns(open('my_file.csv'), headers=['header1', 'header2']) ==\
       {'header1': ['h1', '1', '3'], 'header2': ['h2', '2', '4']}

# bonus 3, allow for rows to have different numbers of columns
assert csv_columns(open('missing.csv'), missing='0') ==\
    {'h1': ['1', '3', '5'], 'h2': ['2', '4', '0']}
assert csv_columns(open('missing.csv')) ==\
    {'h1': ['1', '3', '5'], 'h2': ['2', '4', None]}
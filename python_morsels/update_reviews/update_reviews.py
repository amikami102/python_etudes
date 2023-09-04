# update_reviews.py
"""
A CLI program that updates one csv to include new rows from another csv.

Usage example:
    $ python update_reviews.py all-restaurants.csv 2016-food.csv
"""
import sys
import csv
from operator import itemgetter
from typing import *
from pathlib import Path

from rich import print


def get_index_key(rowdict: dict[str, str], keys: tuple[str]) -> tuple[str, ...]:
    """ Return a tuple of values of `keys` from `rowdict`. """
    return tuple(
        itemgetter(key)(rowdict) for key in keys
    )


if __name__ == '__main__':
    [filename1, filename2] = sys.argv[1:]
    
    index_keys: tuple[str] = ('Name', 'Street')
    

    current: set[tuple[str, ...]] = {
        get_index_key(row, index_keys)
        for row in csv.DictReader(Path(filename1).open())
    }
    
    newrows: list[list[str]] = [
        row.values()
        for row in csv.DictReader(Path(filename2).open())
        if get_index_key(row, index_keys) not in existing
    ]
    
    with Path(filename1).open(mode='at', newline='\n') as f:
        writer = csv.writer(f)
        writer.writerows(newrows)
    print(f'Added {len(newrows)} row(s)')
    
    
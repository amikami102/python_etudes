# fixed2csv.py
"""
A program that will take a fixed-width file and turns it into a csv file.

Usage example:
    $ python fixed2csv.py cars.txt cars.csv --cols=0:4,6:19,24:37
"""
from typing import *
import csv
import argparse


def parse_fixed_width_file(
        file: TextIO,
        start_end_values: list[tuple[int, int]]
    ) -> list[list[str]]:
    """ Return a list of list of row values from file-like object `file` and the column `start_end_values`. """
    return [
        [row_string[start:end].rstrip() for start, end in start_end_values]
        for row_string in file
    ]


def parse_columns(string: str) -> list[tuple[int, int]]:
    """ Parse a string of comma-delimited pairs of colon-delimited numbers, `string`."""
    pairs = (pair.split(':') for pair in string.split(','))
    return [
        (int(start), int(end))
        for start, end in pairs
    ]
        

# base problem, test `parse_fixed_width_file()`
with open('cars.txt') as txt_file:
    rows = list(parse_fixed_width_file(txt_file, [(0, 4), (6, 19), (24, 37)]))
assert rows == [
    ['2012', 'Lexus', 'LFA'],
    ['2009', 'GMC', 'Yukon XL 1500'],
    ['1965', 'Ford', 'Mustang'],
    ['2005', 'Hyundai', 'Sonata'],
    ['1995', 'Mercedes-Benz', 'C-Class'],
]

# bonus 1, test `parse_columns()`
assert list(parse_columns('0:4,6:19,24:37')) == [(0, 4), (6, 19), (24, 37)]

# bonus 2, test the program
if __name__ == '__main__':
    
    # Parse CLI arguments
    parser = argparse.ArgumentParser(
        description='Takes a fixed-width txt file and writes a csv file.'
    )
    parser.add_argument('fixed_width_file', type=argparse.FileType('r'), help='path of input txt file with fixed width columns', )
    parser.add_argument('csvfile', type=argparse.FileType('w'), help='path of output csv file',)
    parser.add_argument('--cols', type=str, help='comma-delimited string of colon-delimited pair of integers indicating column start/end values')
    args = parser.parse_args()
    args.csvfile.reconfigure(newline='')
    
    # Write contents of fixed width file to csv file
    start_end_values = parse_columns(args.cols)
    rows = parse_fixed_width_file(args.fixed_width_file, start_end_values)
    csv.writer(args.csvfile).writerows(rows)
    
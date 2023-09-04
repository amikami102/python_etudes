# sort_by_columns.py
"""
A program that will read a CSV file, sort it by a given column number, and print out th resulting sorted rows.

Usage example:
    $ python sort_by_columns.py colors.csv 0
    $ python sort_by_columns.py colors.csv 1:num
    $ python sort_by_columns.py cars.csv --with-header 2 1 0
"""
from typing import *
import argparse
import sys
from pathlib import Path
import csv


def parse_column_types(column: str) -> tuple[int, str]:
    """Convert colon-separted string, `column`, into a tuple of its partitions."""
    colnum, _, coltype = column.partition(':')
    return int(colnum), coltype if coltype else 'str'


def row_in_sorting_order(column_order: Iterable[str]) -> Callable:
    """
    Return a callable that returns new tuple with the elements of `row` reordered and
    converted into data types specified by `column_order`.
    """
    def key_func(row: tuple[str]) -> tuple[str]:
        column_number_and_types = [parse_column_types(col) for col in column_order]
        return tuple(
            str(row[num]) if coltype == 'str' else int(row[num])
            for num, coltype in column_number_and_types
        )
    return key_func


def main(args: argparse.Namespace) -> None:
    """
    Read the input csvfile and print out the rows sorted by specified column order.
    """
    reader = csv.reader(args.csvfile)
    writer = csv.writer(sys.stdout)
    if args.with_header:
        header = next(reader)
        writer.writerow(header)
    rows = sorted(reader, key=row_in_sorting_order(args.columns))
    writer.writerows(rows)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('csvfile', type=argparse.FileType('r'))
    parser.add_argument('--with-header', action='store_true', help='The first row will be treated as a header')
    parser.add_argument('columns', type=str, nargs='+')
    args = parser.parse_args()
    main(args)

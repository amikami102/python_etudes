# diff_cols.py
"""
A program that acceps two CSV files and slices of columns and print
out diffs of the given columns.

Usage:
    $ python diff_cols.py original.csv new.csv
    --- original.csv
    +++ new.csv
    @@ -2,7 +2,6 @@
     mousepad,rainbow,2005-02-28,256 colors
     desk,black,2010-11-15,
     duck,purple,2015-06-30,
    -duck,pink,2015-06-30,unicorn horn and mane
    -bottle,gray,2016-02-04,a little worn
    -lamp,white,2018-08-02,bought at IKEA
    -lamp,white,2018-08-02,bought at IKEA
    +duck,pink,2015-06-30,blue unicorn horn
    +bottle,silver,2016-02-04,a little worn
    +lamp,beige,2018-08-02,2 of them
    
    $ python diff_cols.py original.csv new.csv --cols=1,-1
    --- original.csv
    +++ new.csv
    @@ -2,7 +2,6 @@
     rainbow,256 colors
     black,
     purple,
    -pink,unicorn horn and mane
    -gray,a little worn
    -white,bought at IKEA
    -white,bought at IKEA
    +pink,blue unicorn horn
    +silver,a little worn
    +beige,2 of them
    
    $ python diff_cols.py original.csv new.csv -c 0 -c 2:
    --- original.csv
    +++ new.csv
    @@ -2,7 +2,6 @@
     mousepad,2005-02-28,256 colors
     desk,2010-11-15,
     duck,2015-06-30,
    -duck,2015-06-30,unicorn horn and mane
    +duck,2015-06-30,blue unicorn horn
     bottle,2016-02-04,a little worn
    -lamp,2018-08-02,bought at IKEA
    -lamp,2018-08-02,bought at IKEA
    +lamp,2018-08-02,2 of them
"""
from typing import *
from difflib import unified_diff
from io import StringIO
import argparse
import csv
import re


SLICE_RE = re.compile(r"""
        ^
        (-? \d*)	# integer
        :
        (-?\d*)?	# optional integer
        :?			# optional colon
        (-? \d*)?	# optional integer
        $
    """,
    re.VERBOSE
)


def slice_rows(rows: list[list[str]], slices: list[slice]) -> Iterable[list[str]]:
    """Slice each inner row in `rows` according to `slices`."""
    if not slices:
        slices = [slice(None, None, None)]
    for row in rows:
        yield [
            col
            for s in slices
            for col in row[s]
        ]


def int_or_none(value: str) -> Optional[int]:
    """Convert `value` into integer or return `None`."""
    return None if not value else int(value)


def slices(string: str) -> Iterable[slice]:
    """
    Return an iterable of slice objects by parsing `string`.
    
    string: str, a comma-delimited string of one or more slices or indexes
    """
    for substring in string.split(','):
        if match := SLICE_RE.match(substring):
            start, stop, step = (int_or_none(n) for n in match.groups())
        else:
            start = int(substring)
            step = 1 if start >= 0 else -1
            stop = start + step
        yield slice(start, stop, step)


def to_csv_lines(rows: list[list[str]]) -> list[str]:
    """Convert `rows` to lines from csv file."""
    lines = StringIO()
    csv.writer(lines).writerows(rows)
    lines.seek(0)
    return list(lines)


def print_diff(
        from_rows: list[list[str]], to_rows: list[list[str]],
        fromfile: str, tofile: str
        ) -> None:
    """Compare `rows1` and `rows2` and print out a unified diff."""
    lines = unified_diff(
        to_csv_lines(from_rows),
        to_csv_lines(to_rows),
        fromfile,
        tofile
    )
    print(*lines, end='', sep='')


# base problem
things = [["A", 10, "z", 2, 0], ["B", 20, "y", 1, 1], ["C", 30, "x", 3, 0]]
assert list(slice_rows(things, [slice(1, None, None)])) ==\
    [[10, 'z', 2, 0], [20, 'y', 1, 1], [30, 'x', 3, 0]]
assert list(slice_rows(things, [slice(0, 2, None), slice(-2, None, None)])) ==\
    [['A', 10, 2, 0], ['B', 20, 1, 1], ['C', 30, 3, 0]]
assert list(slice_rows(things, [slice(None, None, -1)])) ==\
    [[0, 2, 'z', 10, 'A'], [1, 1, 'y', 20, 'B'], [0, 3, 'x', 30, 'C']]
assert list(slice_rows(things, [])) == things

# bonus 1, test `slices()` function
assert list(slices('0:2')) == [slice(0, 2, None)]
assert list(slices('-3:')) == [slice(-3, None, None)]
assert list(slices(':2,-2:')) == [slice(None, 2, None), slice(-2, None, None)]
assert list(slices('::-1')) == [slice(None, None, -1)]
assert list(slices(':2,3')) == [slice(None, 2, None), slice(3, 4, 1)]
m = "Python is fun"
assert "".join(m[s] for s in slices('0,-6,-4:')) == 'Pi fun'

# bonus 2, test `print_diff()` function
file1 = "before.txt"
file2 = "after.txt"
rows1 = [["duck", "purple", ""], ["lamp", "white", ""]]
rows2 = [["duck", "pink", "unicorn horn and mane"], ["lamp", "white", ""]]
print_diff(rows1, rows2, file1, file2)

# bonus 3, test the CLI program
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('file1', type=argparse.FileType('r'))
    parser.add_argument('file2', type=argparse.FileType('r'))
    parser.add_argument('-c', '--cols', action='extend', type=slices, default=[])
    args = parser.parse_args()
    
    rows1 = slice_rows(csv.reader(args.file1), args.cols)
    rows2 = slice_rows(csv.reader(args.file2), args.cols)

    print_diff(rows1, rows2, args.file1.name, args.file2.name)
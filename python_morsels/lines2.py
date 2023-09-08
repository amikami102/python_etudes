# lines2.py
"""
A program that prints the number of lines in various code files.
The program will print out a table of file counts, line counts, and non-blank line counts for html, js, md, and py file extensions.
At the bottom, the total sum of each column will be printed out.
Note that "Extension" column is left-aligned but all the other columns are right-aligned.

Usage example:
    $ python lines2.py lines2
    Extension    Files    Lines    Non-blank
    js               1        1            1
    md               1        9            6
    py               8       25           22
    Total           10       35           29
    
    $ python lines2.py lines2 --ext=py,yml,rst,toml
    Extension    Files    Lines    Non-blank
    py               3       11           10
    Total            3       11           10
    
    $ python lines2.py lines2/a.py lines2/b.py
    Extension    Files    Lines    Non-blank
    py               2        2            2
    Total            2        2            2
"""
from typing import *
import argparse
from pathlib import Path

from count_lines import count_lines, convert_to_list
from format_fixed_width import format_fixed_width


HEADER: tuple[str] = ('Extension', 'Files', 'Lines', 'Non-blank')
EXTENSIONS: list[str] = ['html', 'js', 'md', 'py']
PADDING: int = 4
ALIGNMENTS: tuple[str] = ('L', 'R', 'R', 'R')
TOTAL: str = 'Total'


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'directories',
        type=Path,
        nargs='+',
        help='Directories or files to get stats on'
    )
    parser.add_argument('--ext', type=str, default=None)
    return parser.parse_args()


def get_totals(list_of_rows: list[tuple]) -> tuple:
    """Get the total file, line, and non-blank line counts."""
    _, *tallies_it = zip(*list_of_rows)
    return (TOTAL, *(sum(tallies) for tallies in tallies_it))


def main(dir: Path, extensions: list[str]) -> None:
    """Print out a table listing file content stats grouped by file extension."""
    counts = convert_to_list(count_lines(dir, extensions))
    rows = [HEADER, *counts, get_totals(counts)]
    print(format_fixed_width(rows, padding=PADDING, alignments=ALIGNMENTS))
    
    
if __name__ == '__main__':
    
    args = parse_args()
    main(
        args.directories,
        args.ext.split(',') if args.ext else EXTENSIONS
    )
    
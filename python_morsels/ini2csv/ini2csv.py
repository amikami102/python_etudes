#ini2csv.py
"""
A program that converts an INI-like file to a CSV-like file.
Assume all sections have the same set of options.

Usage example:
    $ python ini2csv.py simple.ini simple.csv
"""
import configparser
import argparse
from pathlib import Path
import csv


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('inifile', type=argparse.FileType('r'))
    parser.add_argument('csvfile', type=argparse.FileType('w'))
    parser.add_argument('--collapsed', action='store_true')
    return parser.parse_args()


def collapse(parser: configparser.ConfigParser) -> list[tuple]:
    """Collapse the data in `parser` to wide form table."""
    options = []
    for section in parser.sections():
        for option in parser.options(section):
            if option not in set(options):
                options.append(option)
    rows = [
        (
            section,
            *(parser[section].get(option, '') for option in options)
        )
        for section in parser.sections()
    ]
    return [('header', *options), *rows]
    

def main() -> None:
    args = parse_args()
    
    # get configuration attributes and values
    parser = configparser.ConfigParser()
    parser.read_file(args.inifile)
    if args.collapsed:
        data = collapse(parser)
    else:
        data = [
            (section, name, value)
            for section in parser.sections()
            for name, value in parser.items(section)
        ]
    
    # Write data to csv
    writer = csv.writer(args.csvfile)
    writer.writerows(data)
    

if __name__ == '__main__':
    main()
    
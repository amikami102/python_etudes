# checksum.py
"""
A program that accepts an md5 checksum file and prints out whether each file in the checksum passes the test.

Usage example:
    $ python checksum.py sums.md5
    $ python checksum.py sums.sha1
    $ python checksum.py check.md5
    $ python checksum.py check.sha1
"""
from typing import *
import sys
import argparse
import hashlib
from pathlib import Path


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('sums_file', type=argparse.FileType('rt'))
    return parser.parse_args()


def get_algorithm(sums_file: TextIO) -> Callable:
    """Get the hashing algorithm used by the `checksum_file`."""
    if sums_file.name.endswith('.md5'):
        return hashlib.md5
    else:
        return hashlib.sha1


def main(args: argparse.Namespace) -> None:
    """
    Get the file hash and file names from `args.sums_file`
    and check against the calculated the file hash.
    Print out a warning message if any errors.
    """
    errors = 0
    algorithm = get_algorithm(args.sums_file)
    for line in args.sums_file:
        checksum, filename = line.split()
        sum_returned = algorithm(Path(filename).read_bytes()).hexdigest()
        if checksum == sum_returned:
            print(f'{filename}: OK')
        else:
            print(f'{filename}: FAILED')
            errors += 1
    if errors:
        print(
            f'WARNING: {errors} computed checksums did not match',
            file=sys.stderr
        )


if __name__ == '__main__':
    args = parse_args()
    main(args)
        
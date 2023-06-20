# remove_empty.py
"""
A script that removes all empty directories recursively.

Usage example:
    $ python remove_empty.py [directory]
"""
from argparse import ArgumentParser
from os import scandir, walk
from pathlib import Path


def is_not_empty(directory):
    """Return True if the given directory is not empty."""
    return not next(scandir(directory), None)


def remove_empty(directory):
    """Remove all empty directories recursively."""
    for path, _, _ in walk(directory, topdown=False):
        if is_not_empty(path):
            path = Path(path)
            print(f"Deleting directory {path.name}")
            path.rmdir()


def main():
    parser = ArgumentParser()
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()
    remove_empty(args.directory)


if __name__ == "__main__":
    main()

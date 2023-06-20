# last_lines.py
"""
A script defining `last_lines()`, which returns lines in an ASCII text file in reverse order.
"""
from typing import *
from pathlib import Path


def last_lines(filename: str) -> Iterable[str]:
    """ Read a file in reverse order. """
    #yield from reversed(list(open(filename)))
    yield from reversed(list(Path(filename).open()))


# base problem and bonus 1
for line in last_lines('my_file.txt'):
    print(line, end='')
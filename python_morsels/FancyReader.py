# FancyReader.py
"""
A script implementing `FancyReader` function.
"""
from rich import print
from typing import *
from textwrap import dedent
import csv
from collections import namedtuple


def FancyReader(rows: Iterable[str], fieldnames: list[str]) -> Iterator[tuple]:
    Row = namedtuple('Row', fieldnames)
    if isinstance(rows, str):
        rows = rows.splitlines()
    return (
        Row(*row)
        for row in csv.reader(rows)
    )


# base problem
lines = ['my,fake,file', 'has,two,rows']
reader = FancyReader(lines, fieldnames=['w1', 'w2', 'w3'])
for row in reader:
    print(row.w1, row.w2, row.w3)

text = dedent("""
            Julia,Spender,purple,Two in the hand is worth one in the fridge
            Sarah,Taylor,green,"Learn from yesterday, live for today"
            Gary,Richter,blue,Be someone you would be proud to know
            Kathleen,Blocker,red,Live everyday like it's your last
            Angelo,Griffith,pink,Don't do today what you could do tomorrow
""").lstrip()
reader = FancyReader(
    text.splitlines(),
    fieldnames=['first', 'last', 'color', 'saying'],
)
rows = list(reader)
print(rows)

# FancyReader.py
"""A script implementing a custom CSV reader class."""
from typing import Iterator, Iterable
import csv
from collections import namedtuple


class FancyReader:
    """A custom CSV reader class."""
    
    def __init__(self,
            csvfile: Iterator[str],
            fieldnames: Iterable[str] = None,
            dialect: str = 'excel',
            **fmtparams
        ):
        self.reader = csv.reader(csvfile, dialect, **fmtparams)
        self.line_num = 0
        self.fieldnames = fieldnames
        self.Row = None
    
    def __next__(self) -> tuple[str]:
        if not self.Row:
            if not self.fieldnames:
                self.fieldnames = next(self.reader)
                self.line_num += 1
            self.Row = namedtuple('Row', self.fieldnames)
        row = self.Row(*next(self.reader))
        self.line_num += 1
        return row 
    
    def __iter__(self) -> 'FancyReader':
        return self
    

# base problem
lines = ['my,fake,file', 'has,two,rows']
reader = FancyReader(lines, fieldnames=['w1', 'w2', 'w3'])
row = next(reader)
assert row.w1 == 'my' and row.w2 == 'fake' and row.w3 == 'file'
row = next(reader)
assert row.w1 == 'has' and row.w2 == 'two' and row.w3 == 'rows'

from textwrap import dedent
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
row1 = next(reader)
assert row1.color == 'purple'
row2 = next(reader)
assert row2.saying == "Learn from yesterday, live for today"

# bonus 1, test that `Row` is iterable and has nice string representation
lines = ['my,fake,file', 'has,two,rows']
reader = FancyReader(lines, fieldnames=['w1', 'w2', 'w3'])
row = next(reader)
assert str(row) == "Row(w1='my', w2='fake', w3='file')"
w1, w2, w3 = row
assert w3 == 'file'

# bonus 2, test that `fieldnames` attribute is optional
lines = ['w1,w2,w3', 'my,fake,file', 'has,two,rows']
reader = FancyReader(lines)
row = next(reader)
assert [row.w1, row.w2, row.w3] == ['my', 'fake', 'file']

# bonus 3, test `line_num` attribute
lines = 'red,1\nblue,2\ngreen,3'.splitlines()
reader = FancyReader(lines, fieldnames=['color', 'number'])
next(reader)
assert reader.line_num == 1
next(reader)
assert reader.line_num == 2

lines = ['w1,w2,w3', 'my,fake,file', 'has,two,rows']
reader = FancyReader(lines)
next(reader)
assert reader.line_num == 2

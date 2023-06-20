# FancyReader2.py
"""
A script implementing `FancyReader` class.
"""
from typing import *
import csv
from collections import namedtuple
from textwrap import dedent
from io import StringIO


class FancyReader:
    """
    A class that accepts an iterable or a file-like ojbect and parses CSV data from that object.
    
    Attributes:
    ----
        delimiter: str, default ','
            the delimiter character of the CSV
        
        fieldnames: None or Iterable[str]
            a list of field names
        
        reader: csv.reader
            rows of CSV
    """
    
    def __init__(self, lines: Iterable[str] | StringIO, *, fieldnames: Optional[Iterable[str]] = None, delimiter: str = ',') -> None:
        """
        Inputs
        ----
            lines: Iterable[str] | StringIO
                list of lines or text stream, basically anything that can be passed into `csv.reader()`
                
            fieldnames: Optional[Iterable[str]]
                optional, a list of field names
                
            delimiter: str, default ','
                the delimiter character of the CSV
        """
        self.delimiter: str = delimiter
        self.fieldnames: Iterable[str] = fieldnames
        self.rows = csv.reader(lines, delimiter=self.delimiter)
        
    def __next__(self) -> Iterable[str]:
        if not self.fieldnames:
            self.fieldnames = next(self.rows)
            
        Row = namedtuple('Row', self.fieldnames)
        row = next(self.rows)
        return Row(*row)
    
    def __iter__(self) -> 'FancyReader':
        return self
        

# base problem and bonus 1
lines = ['w1|w2|w3', 'my|fake|file', 'has|two|rows']
reader = FancyReader(lines, delimiter='|')
row = next(reader)
assert (row.w1, row.w2, row.w3) == ('my', 'fake', 'file')

my_file = StringIO("a,b,c\r\n1,2,3\r\n4,5,6\r\n")
reader = FancyReader(my_file)
assert len(list(reader)) == 2

text = dedent("""
    first,last,color,saying
    Julia,Spender,purple,Two in the hand is worth one in the fridge
    Sarah,Taylor,green,"Learn from yesterday, live for today"
    Gary,Richter,blue,Be someone you would be proud to know
    Kathleen,Blocker,red,Live everyday like it's your last
    Angelo,Griffith,pink,Don't do today what you could do tomorrow
""").lstrip()
reader = FancyReader(text.splitlines())
rows = list(reader)
assert len(rows) == 5

my_file = StringIO("a,b,c\r\n1,2,3\r\n4,5,6\r\n")
reader = FancyReader(x for x in my_file)
assert my_file.tell() == 0
assert tuple(next(reader)) == ('1', '2', '3')
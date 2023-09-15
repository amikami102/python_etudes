# jot.py
"""
A program that saves idea long with the current date in a jot.txt file.

Usage example:
    $ python jot.py
"""
import sys
from datetime import date
from pathlib import Path


text = input("jot: ")
jotfile = Path('jot.txt')
with jotfile.open('at') as f:
    print(date.today(), text, file=f)

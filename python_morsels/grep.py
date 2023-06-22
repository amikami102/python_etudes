# grep.py
"""
A program that implements `grep` Linux/Unix command-line program.

Usage examples:
    $ python grep.py to dickinson.txt
    Are you – Nobody – too?
    How dreary – to be – Somebody!
    
    $ python grep.py Nobody dickinson.txt scrambled.txt
    dickinson.txt:I'm Nobody! Who are you?
    dickinson.txt:Are you – Nobody – too?
    scrambled.txt:How public – to be – Nobody!
    scrambled.txt:To an admiring Nobody!
    
    $ python grep.py Are dickinson.txt -i
    I'm Nobody! Who are you?
    Are you – Nobody – too?
    
    $ python grep.py --ignore-case FROG dickinson.txt scrambled.txt
    dickinson.txt:How public – like a Frog –
    scrambled.txt:I'm Frog! Who are you?
    
    $ python grep.py '.* .* .* .* .* .* .*' dickinson.txt
    Don't tell! they'd advertise – you know!
    How dreary – to be – Somebody!
    How public – like a Frog –
    To tell one's name – the livelong June –
    
    $ python grep.py Nobody dickinson.txt scrambled.txt --line-number
    dickinson.txt:1:I'm Nobody! Who are you?
    dickinson.txt:2:Are you – Nobody – too?
    scrambled.txt:6:How public – to be – Nobody!
    scrambled.txt:9:To an admiring Nobody!
    
    $ python grep.py '!$' dickinson.txt -n
    3:Then there's a pair of us!
    4:Don't tell! they'd advertise – you know!
    6:How dreary – to be – Somebody!
    9:To an admiring Bog!
"""
from typing import *
import argparse
import re
from pathlib import Path

from rich import print


parser = argparse.ArgumentParser('Search for the string pattern in files')
parser.add_argument('pattern', type=str, help='String pattern to look for')
parser.add_argument('files', nargs='*', help='Files in which to look for the string pattern')
parser.add_argument('--ignore-case', '-i', action='store_true', help='Ignore case')
parser.add_argument('--line-number', '-n', action='store_true', help='Show line number')
args = parser.parse_args()

pattern = re.compile(args.pattern, re.I if args.ignore_case else 0)

for file in args.files:
    for i, line in enumerate(Path(file).open(mode='r'), start=1):
        if pattern.search(line):
            print(f'{file}:' if len(args.files) > 1 else '', end='')
            print(f'{i}:{line}' if args.line_number else line, end='')

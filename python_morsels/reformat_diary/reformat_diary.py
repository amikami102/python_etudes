# reformat_diary.py
"""
A program that turns a text file with many diary entries into many text files, one for each entry.

Assume that
    - entry date are all formatted YYYY-MM-DD;
    - all entries are preceded by the date marking the entry.

Usage example:
    $ python reformat_diary.py my_diary.txt
    2018-01-01.txt written
    2018-01-02.txt written
"""
from typing import *
import sys
from pathlib import Path
import re

DATE_RE = re.compile('\d{4}-\d{2}-\d{2}')


def replace_html_escapes(text: str) -> str:
    """
    Replace HTML escape entities.
    Specifically, replace
        - '&nbsp;' wth a single whitespace,
        - '&quot;' with double quote character, and
        - '&amp' with ampersand.
    """
    return text.replace('&nbsp;', ' ').replace('&quot;', '"').replace('&amp;', '&')


def entries_by_date(diary: TextIO) -> Iterator[tuple[str, str]]:
    """
    Take `diary` text file object and return a list of two-tuples containing the date and corresponding entry.
    Preserve the newlines between the entry texts.
    """
    cur_date = None
    
    for line in diary:
        if matched := DATE_RE.match(line):
            if cur_date:	# yield the existing entry
                yield cur_date, ''.join(cur_entry).strip()
            cur_date = matched.group()
            cur_entry = []
        else:
            cur_entry.append(replace_html_escapes(line))
    # yield the last entry
    yield cur_date, ''.join(cur_entry).strip()


def main(filename: str) -> None:
    """
    Create a separate file for each diary entry in file named `filename`.
    The diary entry for date YYYY-MM-DD should be written in 'YYYY-MM-DD.txt'.
    """
    diary_path = Path(filename)
    with open(diary_path) as diary_file:
        for date, entry in entries_by_date(diary_file):
            newfile = f'{date}.txt'
            Path(newfile).write(entry)
            print(newfile, 'written')
    
    

# base problem, test `entries_by_date()` without HTML artifacts
diary_file = open('my_diary.txt')
assert list(entries_by_date(diary_file)) ==\
    [
        ('2018-01-01', 'Coded.\n\nDid laundry.'),
        ('2018-01-02', 'Slept all day.')
    ]

# bonus 1, test that `entries_by_date()` can remove HTML artifacts
diary_file = open('my_diary2.txt')
assert list(entries_by_date(diary_file)) ==\
    [
        ('2018-01-01', 'I said "rabbit, rabbit" today.'),
        ('2018-01-02', 'I slept all day.  I ate fish & chips.')
    ]

# bonus 2, test `main()` and the whole program
if __name__ == '__main__':
    
    [*filenames] = sys.argv[1:]
    for filename in filenames:
        main(filename)
    

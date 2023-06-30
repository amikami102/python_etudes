# pattern_rename.py
"""
A program that can find files with one naming scheme and help rename them according to a different naming scheme.
"""
from typing import *
import re

PARTS_RE = re.compile(r'%([A-Z])')


def scan(scanf_pattern: str, filename: str) -> Optional[dict]:
    """ Parse `filename` to extract a dictionary of `pattern` parts. If no match found, return `None`."""
    regex = PARTS_RE.sub(r'(?P<\1>.+?)', re.escape(scanf_pattern))
    if match := re.fullmatch(regex, filename):
        return match.groupdict()
    return None
    
def format(scanf_pattern, pattern_parts: dict) -> str:
    """ Return a new filename constructed by joining `pattern_parts`. """
    format_string = PARTS_RE.sub(r'{\1}', scanf_pattern)
    return format_string.format(**pattern_parts)


# base problem, test `scan()` and `format()`
pattern, filename = "%A/%B/%N - %T.mp3", "Nirvana/Nevermind/02 - In Bloom.mp3"
assert scan(pattern, filename ) == {'A': 'Nirvana', 'B': 'Nevermind', 'N': '02', 'T': 'In Bloom'}

parts = scan("%A/%B/%N - %T.mp3", "Nirvana/Nevermind/In Bloom.mp3")
assert not parts

data = {'A': "Nirvana", 'B': "Nevermind", 'N': "02", 'T': "In Bloom"}
assert format("%A - %B/%N %T.mp3", data) == 'Nirvana - Nevermind/02 In Bloom.mp3'


# bonus 1, escape special characters other than % and match characters conservatively
assert scan("%B [%Y]/%T.mp3", "Still Bill [1972]/Lean On Me.mp3")\
    == {'B': 'Still Bill', 'Y': '1972', 'T': 'Lean On Me'}
assert scan("%B/%N %T.mp3", "Tapestry/01 I Feel The Earth Move.mp3")\
    == {'B': 'Tapestry', 'N': '01', 'T': 'I Feel The Earth Move'}
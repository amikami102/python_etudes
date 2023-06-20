# CountVotes.py
"""
A script that receives individual votes on topics
and returns the vote tally.
"""
from rich import print
from typing import *
import re
import itertools
import collections
import sys
import pathlib


def get_vote_tally(input_string: str) -> Iterable[tuple]:
    """
    Find all numbers in the string
    """
    out = {}
    votes = sorted(map(int, re.findall(r'[\d\.]+', input_string)))
    for k, v in collections.Counter(votes).items():
        out.setdefault(v, [])
        out[v].append(k)
    return sorted(out.items(), reverse=True)


if __name__ == '__main__':
    
    test1 = "Victor: 1 3 4\nPaul: 1 3\nAlex: 2 3 4\nMildred: 2 4\n"
    test2 = """\
    Mary:
    40, 50
    Jessie:
    40,20,30
    Gabriel:
    30 20 & 50
    Ella:
    10 20 40, but I'm fine with any
    Sarah:
    20 30 50!!
    Read:
    10 20 40
    30 40 50 (from Meagan earlier in chat)
    """
    [file] = sys.argv[1:]
    test3 = pathlib.Path(file).read_text()
    test4 = ''
    
    test = test3
    
    if not test:
        pass
    else:
        for n, candidates in get_vote_tally(test):
            print(f"{n} votes for: {', '.join(map(str, candidates))}")

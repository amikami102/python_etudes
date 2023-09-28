# CountVotes.py
"""
A module/script that accepts a filename that contains individual votes on
topics represented by numbers and prints the vote tally.
"""
from typing import *
import re
from itertools import groupby
from collections import Counter
from operator import itemgetter


def get_vote_tally(vote_string: str) -> Iterable[tuple[int, list[int]]]:
    """
    Return an iterable of two-item tuples where the first
    item is the vote count and the second item lists the choices
    mentioned in `vote_string`. All choices are numbers.
    """
    counted: list[tuple[str, int]] = Counter(
            re.findall('\d+', vote_string)
        ).most_common()
    return [
        (key, sorted([int(choice) for (choice, _) in group]))
        for key, group in groupby(counted, key=itemgetter(1))
    ]
        
    
    
# base problem, test `get_vote_tally()` function
assert get_vote_tally(
    "Victor: 1 3 4\nPaul: 1 3\nAlex: 2 3 4\nMildred: 2 4\n"
    ) == [(3, [3, 4]), (2, [1, 2])]
assert get_vote_tally("""
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
    """) == [(5, [20, 40]), (4, [30, 50]), (2, [10])]


# bonus 1, test the program
if __name__ == '__main__':
    import sys
    from pathlib import Path
    
    try:
        [file] = sys.argv[1:]
    except ValueError:
        vote_txt = input('Paste all options')
    else:
        tally = get_vote_tally(Path(file).read_text())
    
    for n, choices in tally:
        s = 's' if n > 1 else ''
        print(n, "vote{s} for: ", end='')
        print(*choices, sep=', ')

# divide.py
"""
A script implementing `divide` function.

10 mod 4 = 2, 2
0, 1, 2 = seq[0: 3] = seq[0 + 0: 1 * 2 + min(1, 2)]
3, 4, 5 = seq[3: 6] = seq[1 * 2 + 1: 2 * 2 + 2]
6, 7, = seq[6: 8] = seq[2 * 2 + 2: 3 * 2 + min(2, 3)]
8, 9 = [8: 10]
"""
from rich import print
from typing import *

T = TypeVar('T')


def divide(sequence: Sequence[T], n: int) -> list[list[T]]:
    """
    Divide `sequence` into a list of `n` lists. 
    """
    q, r = divmod(len(sequence), n)
    return [
        sequence[i * q + min(i, r): (i + 1) * q + min(i + 1, r)]
        for i in range(n)
    ]


for chunk in divide([1, 2, 3, 4, 5], 2):
    print(*chunk)

for chunk in divide(range(10), 4):
    print(tuple(chunk))

for chunk in divide([1, 2, 3, 4, 5], n=7):
    print(tuple(chunk))
    
# divide.py
"""
A script implementing `divide()` function.

divmod(10, 4) = 2, 2
0, 1, 2 = seq[0: 3] = seq[0 + 0: 1 * 2 + min(1, 2)]
3, 4, 5 = seq[3: 6] = seq[1 * 2 + min(1, 2): 2 * 2 + min(2, 2)]
6, 7 = seq[6: 8] = seq[2 * 2 + min(2, 2): 3 * 2 + min(3, 2)]
8, 9 = seq[8: 10] = seq[3 * 2 + min(3, 2): 4 * 2 + min(4, 2)]
"""
from typing import *
from itertools import islice, chain, repeat

T = TypeVar('T')
NO_FILL = object()


def divide(
        iterable: Iterable[T], n: int, *, length: int = None, fill: T = NO_FILL
    ) -> Iterable[list[T]]:
    """Divide `iterable` into `n` sublists."""
    if length is None:
        length = len(iterable)
    q, r = divmod(length, n)
    
    it = iter(iterable)
    if fill is not NO_FILL and r != 0:
        it = chain(it, repeat(fill, n - r))
        r = n
    for i in range(n):
        yield list(islice(it, q + (i < r)))


# base problem
assert list(divide([1, 2, 3, 4, 5], n=2)) == [[1, 2, 3], [4, 5]]
assert [tuple(d) for d in divide(range(10), 4)] ==\
    [(0, 1, 2), (3, 4, 5), (6, 7), (8, 9)]
assert list(divide([1, 2, 3, 4, 5], n=7)) ==\
    [ [1], [2], [3], [4], [5], [], []]

# bonus 1, test that `divide()` returns an iterator
sections = divide([1, 2, 3, 4, 5], n=2)
assert tuple(next(sections)) == (1, 2, 3)

# bonus 2, accept any iterable
squares = (n**2 for n in range(6))
sections = divide(squares, n=3, length=6)
next(sections)
assert tuple(next(sections)) == (4, 9)

# bonus 3, test `fill` argument
sections = divide(range(10), n=4, fill=0)
# next(sections)
# next(sections)
# next(sections)
# assert tuple(next(sections)) == (9, 0, 0)
# print(tuple(next(sections)))
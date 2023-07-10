# smoosh.py
"""
A script defining utilities that flatten an iterable of iterables `n` levels deep.
"""
from typing import *
import re
from functools import partial

T = TypeVar('T')
SMOOSH_RE = re.compile(r'^smoo+sh$')

def _smoosh(nested_iterable: Iterable[Iterable[T]], n: int = 1) -> Iterator[T]:
    """ Generate a flattened `nested_iterable` `n` level deep. """
    for sublist in nested_iterable:
        if isinstance(sublist, Iterable) and not isinstance(sublist, str) and n:
            yield from smoosh(sublist, n - 1)
        else:
            yield sublist

smoosh = _smoosh
smooosh = partial(_smoosh, n=2)
smoooosh = partial(_smoosh, n=3)
smooooosh = partial(_smoosh, n=4)
smoooooosh = partial(_smoosh, n=5)
smooooooosh = partial(_smoosh, n=6)


def __getattr__(name: str) -> Callable:
    """ Add any variant of `_smoosh` to the module by making a dynamic attribute. """
    if SMOOSH_re.match(name):
        levels = len(name.lstrip('smo').rstrip('sh'))
        return partial(_smoosh, n=levels)
    else:
        raise AttributeError(f"module {__name__} has no attribute {name}")
    

# base problem, test `smoosh()`
matrix = [[1, 2, 3], [4, 5, 6]]
assert list(smoosh(matrix)) == [1, 2, 3, 4, 5, 6]
matrix = [1, 2, [3, 4], 5, 6]
assert list(smoosh(matrix)) == [1, 2, 3, 4, 5, 6]
matrix = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
assert list(smoosh(matrix)) == [[1, 2], [3, 4], [5, 6], [7, 8]]
words = ['Python', 'is', 'lovely']
assert list(smoosh(words)) == ['Python', 'is', 'lovely']
pairs = [(1, 'I'), (5, 'V'), (10, 'X'), (50, 'L'), (100, 'C')]
assert list(smoosh(pairs)) == [1, 'I', 5, 'V', 10, 'X', 50, 'L', 100, 'C']

# bonus 1, test n >=2 levels of flattening
data = [
        2,
        [
            [
                1,
                [
                    3,
                    [
                        4,
                        7,
                        [
                            11,
                            [
                                18,
                                29,
                            ],
                            40,
                            69,
                        ],
                        109,
                    ],
                ],
                178,
            ],
        ],
    ]
assert list(smoosh(data)) == [2, [1, [3, [4, 7, [11, [18, 29], 40, 69], 109]], 178]]
assert list(smooosh(data)) == [2, 1, [3, [4, 7, [11, [18, 29], 40, 69], 109]], 178]
assert list(smoooosh(data)) == [2, 1, 3, [4, 7, [11, [18, 29], 40, 69], 109], 178]
assert list(smooooosh(data)) == [2, 1, 3, 4, 7, [11, [18, 29], 40, 69], 109, 178]
assert list(smoooooosh(data)) == [2, 1, 3, 4, 7, 11, [18, 29], 40, 69, 109, 178]
assert list(smooooooosh(data)) == [2, 1, 3, 4, 7, 11, 18, 29, 40, 69, 109, 178]

# bonus 2, make the module `smoosh` support any variant of `smoosh` function
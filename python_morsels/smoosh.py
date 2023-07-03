# smoosh.py
"""
A script defining utilities that flatten an iterable of iterables `n` levels deep.
"""
from typing import *
from functools import partial

T = TypeVar('T')

def smoosh(nested_iterable: Iterable[Iterable[T]], n: int = 1) -> Iterator[T]:
    """ Generate a flattened `nested_iterable` `n` level deep. """
    for sublist in nested_iterable:
        if isinstance(sublist, Iterable) and not isinstance(sublist, str) and n:
            yield from smoosh(sublist, n - 1)
        else:
            yield sublist


smooosh = partial(smoosh, n=2)
smoooosh = partial(smoosh, n=3)
smooooosh = partial(smoosh, n=4)
smoooooosh = partial(smoosh, n=5)
smooooooosh = partial(smoosh, n=6)

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
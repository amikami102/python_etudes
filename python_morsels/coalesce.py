# coalesce.py
"""
A script defining `coalesce()` function, which implements null coalescing.
"""
from typing import *

T = TypeVar('T')
S = TypeVar('Sentinel')


def coalesce(*args, sentinel: Optional[S]|Iterable[S] = None) -> T:
    """ Return the first argument in `args` that isn't one of the sentinel values. """
    sentinels = (sentinel, ) if not isinstance(sentinel, tuple) else sentinel
    for arg in args:
        if arg not in sentinels:
            return arg
    raise ValueError(f'All given values were equal to one of {sentinels}')

    
# base problem
name = "Trey"
assert coalesce(name, "") == 'Trey'
name = None
assert coalesce(name, "") == ''

assert coalesce("Trey", []) ==  "Trey"
assert coalesce("", []) == ""
assert coalesce(None, []) == []
assert coalesce([1, 2, 3], []) == [1, 2, 3]
x = []
assert coalesce(x, []) == x
assert coalesce(x, []) is x


# bonus 1, test the keyword argument `sentinel`
name = "Trey"
assert coalesce(name, "world", sentinel="") == 'Trey'
name = ""
assert coalesce(name, "world", sentinel="") == 'world'
name = None
assert coalesce(name, "world", sentinel="") is None

name = "Trey"
assert coalesce(name, "world", sentinel=("", None)) == 'Trey'
name = ""
assert coalesce(name, "world", sentinel=("", None)) == 'world'
name = None
assert coalesce(name, "world", sentinel=("", None)) == 'world'

# bonus 2, test that `coalesce()` accepts any number of arguments and returns the first argument that isn't a sentinel
(short_name, long_name) = ("Trey", "Trey Hunner")
assert coalesce(short_name, long_name, "you", sentinel=("", None)) == 'Trey'

(short_name, long_name) = ("Trey", "")
assert coalesce(short_name, long_name, "you", sentinel=("", None)) == 'Trey'

(short_name, long_name) = ("", "Trey Hunner")
assert coalesce(short_name, long_name, "you", sentinel=("", None)) == 'Trey Hunner'

(short_name, long_name) = ("", "")
assert coalesce(short_name, long_name, "you", sentinel=("", None)) == 'you'

try:
    coalesce(None, None, None, None, None, sentinel=None)
except ValueError as e:
    print('error raised as expected')
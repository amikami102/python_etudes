# is_iterator.py
"""
A script defining three versions of `is_iterator()`, a function that returns True if the given iterable is an iterator.
"""
def is_iterator1(iterable) -> bool:
    # not only is it equal, but identical
    return iter(iterable) is iterable

def is_iterator2(iterable) -> bool:
    return hasattr(iterable, '__next__')

def is_iterator3(iterable) -> bool:
    from typing import Iterator
    return isinstance(iterable, Iterator)

is_iterator = is_iterator2

# base problem
assert is_iterator(iter([]))
assert not is_iterator([1, 2])
i = iter([1, 2])
assert is_iterator(i)
assert list(i) == [1, 2]
def gen(): yield 4
assert is_iterator(gen())
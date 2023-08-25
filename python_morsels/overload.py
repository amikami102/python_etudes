# overload.py
"""
A scipt defining a decorator class, `overload()`, which works like `functools.singledispatch`.
"""
from typing import *
from collections import defaultdict
import functools


class overload:
    """
    A decorator class that overloads functions based on how many arguments they accept and what their type are.
    
    Attributes:
    ------
        registry: dict
            a nested dictionary whose outer keys are the id's of the decorated functions
            and the inner keys are the tuple of argument types
        
        wrappers: dict
            a mapping of id to a wrapper function
        
        id: str | Callable
            the id of the decorated function
        
        types: tuple[type, ...]
            the types of the arguments passed into the decorated function
    """    
    registry: dict[str|Callable, list[tuple[type,...], Callable]] = defaultdict(list)
    wrappers: dict[str|Callable, Callable] = {}
    
    
    def __init__(self, *types, id: str|Callable = None):
        self.id = getattr(id, '__wrapped__', id)
        self.types: tuple[type] = types
    
    def __call__(self, func: Callable) -> Callable:
        """
        This is called whenever `func` is decorated.
        Return another callable, `self.wrapper`, which returns the wrapped function.
        """
        if self.id is None:
            self.id = func
            
        self.functions: list = self.registry.setdefault(self.id, [])
        self.functions.append((self.types, func))
        
        if self.id not in self.wrappers:
            self.wrappers[self.id] = self._make_wrapper(func)
        
        return self.wrappers[self.id]
    
    
    def _make_wrapper(self, func: Callable) -> Callable:
        """
        This is called the first time the `id` is added to `wrappers`.
        """
        @functools.wraps(func)
        def wrapper(*args):
            """
            Find the first entry in `functions` attribute that matches the type map of `args` and
            return the output of that function on `args`. Otherwise, raise TypeError.
            """
            for types, func in self.functions:
                if len(args) == len(types) and \
                   all(isinstance(a, t) for a, t in zip(args, types)):
                    return func(*args)
            raise TypeError('Invalid arguments supplied')
        return wrapper
    
       
# base problem
@overload(list, list, id='add')
def add(seq1, seq2):
    return [x+y for x, y in zip(seq1, seq2)]

@overload(list, int, id='add')
def add(sequence, n):
    return [x+n for x in sequence]

@overload(int, list, id='add')
def add(n, sequence):
    return [x+n for x in sequence]

@overload(int, int, id='subtract')
def subtract(n, m):
    return n-m

assert add([1, 2, 3], 2) == [3, 4, 5]
assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
assert add(2, [1, 2, 3]) == [3, 4, 5]
assert subtract(2, 3) == -1

# raise TypeError if the types and/or number of arguments aren't expected
try:
    add(3, 4)
except TypeError:
    print('passed')
else:
    print('failed')

@overload(id='do_stuff')
def do_stuff():
    return (0,)
@overload(str, id='do_stuff')
def one(x):
    return (1, x)

assert do_stuff('a') == (1, 'a')

# bonus 1, make sure `overload` works for subclasses, abstract types, and tuples of multiple types
import math
@overload((int, float), id='sqrt')
def sqrt(n):
    if n >= 0:
        return math.sqrt(n)
    else:
        return sqrt(n+0j)

import cmath
@overload(complex, id='sqrt')
def sqrt(n):
    return cmath.sqrt(n)

from decimal import Decimal
@overload(Decimal, id='sqrt')
def sqrt(decimal):
    return decimal.sqrt()

from collections.abc import Iterable
@overload(Iterable, id='sqrt')
def sqrt(iterable):
    return sqrt(sum(n**2 for n in iterable))

assert sqrt(4) == 2.0
assert sqrt(-1) == 1j
assert sqrt(Decimal('5')) == Decimal('2.236067977499789696409173669')
assert round(sqrt([1, 2, 3]), 2) == 3.74
assert sqrt([2, 6, 3]) == 7.0

# bonus 2, make sure the decorated function maintains the name and docstring of the first overloaded function
# (i.e. the first time each `id` is used)
overload.registry.clear()
overload.wrappers.clear()

@overload(list, list, id='add_all')
def add_all(seq1, seq2):
    """Add a sequence to another sequence or to an integer."""
    return [x+y for x, y in zip(seq1, seq2)]

@overload(list, int, id='add_all')
def add_all(sequence, n):
    return [x+n for x in sequence]

@overload(int, list, id='add_all')
def add_all(n, sequence):
    return [x+n for x in sequence]

assert 'Add a sequence to another sequence or to an integer' in add_all.__doc__ 
    
# bonus 3, allow `id` to be the original `overload`-decorated function
overload.registry.clear()

@overload(int, int)
def add(x, y):
    return x + y
@overload(str, str, id=add)
def add(x, y):
    return x + y
@overload(str, int, id=add)
def add(x, y):
    return x + str(y)
@overload(int, str, id=add)
def add(x, y):
    return str(x) + y

assert add(1, '2') == '12'
assert add(1, 2) == 3

# overload.py
"""
A scipt defining `overload()` decorator which works like a simplified version of `functools.singledispatch`.
"""
from typing import *
from itertools import count


class overload:
    """
    A decorator that overloads functions based on how many arguments they accept and what their type are.
    
    A class-level attribute `registry` is a nested dictionary whose outer keys are the
    string id's of functions and the inner keys are the tuple of argument types.
    
    When a decorated function is called, the appropriate version of the function will be looked up in `registry`.
    """
    
    registry: dict[str, dict[tuple[type,...], Callable]] = {}
    
    def __init__(self, *types, id: str):
        self.registry.setdefault(id, {})
        self.id = id
        self.types = types
    
    def __call__(self, func: Callable) -> Callable:
        """
        This is called whenever `func` is decorated.
        Return another callable, `self.wrapper`, which returns the wrapped function.
        """
        name = func.__name__
        self.registry[self.id][self.types] = func
        
        def wrapper(*args):
            """
            This is the code executed whenever the decorated function is called.
            Look up whether the argument types a/o numbers passed in the function has been registered.
            """
            argtypes = tuple(type(arg) for arg in args)
            try:
                return self.registry[self.id][argtypes](*args)
            except KeyError:
                # raise from None to avoid chaining exceptions
                raise TypeError('Invalid arguments supplied') from None
        
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
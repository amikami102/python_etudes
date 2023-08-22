# record_calls.py
"""
A script defining a decorator function, `record_calls`,
that records the number of times a function is called.

Tags: decorator function, adding attribute to a function
"""
from typing import *
from dataclasses import dataclass, field
from collections import defaultdict
from functools import wraps

T = TypeVar('T')
NO_RETURN = object()

@dataclass
class Call:
    args: tuple = field(default=())
    kwargs: dict = field(default=None)
    return_value: T = field(default=NO_RETURN)
    exception: Exception = field(default=None)


def record_calls(func: Callable) -> Callable:
    """ Return a version of `func` that record calls made on it."""
    @wraps(func)
    def new_func(*args, **kwargs) -> T:       
        # update attributes, `call_count` and `calls`
        new_func.call_count += 1
        new_func.calls.append(Call(args, kwargs))
        call = new_func.calls[-1]
        try:
            return_value = func(*args, **kwargs)
        except BaseException as exc:
            call.exception = exc
            raise
        else:
            call.return_value = return_value
            return return_value
        
    new_func.call_count: int = 0
    new_func.calls: list[Call] = []
    return new_func


# base problem, test `call_count` attribute
@record_calls
def greet(name="world"):
    """Greet someone by their name."""
    print(f"Hello {name}")

greet('cage')
assert greet.call_count == 1
greet()
assert greet.call_count == 2

# bonus 1, preserve the name, docstring, and call signature of the original function
print(help(greet))

# bonus 2, test `calls` attribute
@record_calls
def greet(name="world"):
    """Greet someone by their name."""
    print(f"Hello {name}")
    
greet('rita')
assert greet.calls[0].args == ('rita',)
assert greet.calls[0].kwargs == {}
greet(name='rita')
assert greet.calls[1].args == ()
assert greet.calls[1].kwargs == {'name': 'rita'}

# bonus 3, test `return_value` and `exception` attributes
@record_calls
def cube(n):
    return n**3

cube(3)
assert cube.calls == [Call(args=(3,), kwargs={}, return_value=27, exception=None)]
try:
    cube(None)
except TypeError:
    assert cube.calls[-1].exception is not None
    assert cube.calls[-1].return_value == NO_RETURN
else:
    print('failed')
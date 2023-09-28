# ratelimit.py
"""
A script defining `ratelimit` decorator, which will ensure that the
decorated function isn't called more than a specified number of times
per second.
"""
from typing import *
from functools import wraps
import time

class ratelimit:
    """A decorator class that sets a rate limit on the decorated function."""
    def __init__(self, per_second: int):
        pass

    def __call__(self, func):
        pass
        

@ratelimit(per_second=3)
def greet(name):
    print('hello', name)
    
greet('me')
greet('me')
greet('me')
try:
    greet('me') # should raise error
except Exception:
    print('passed')
else:
    print('failed')
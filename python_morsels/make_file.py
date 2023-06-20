# make_file.py
"""
A script defining a context manager `make_file` that will create a temporary file that exists only within its `with` block.
"""
from typing import *
import tempfile
import os

from rich import print


class make_file:
    """ Context manager for creating temporary files. """
    
    def __init__(self, contents: str=None):
        """ If `contents` is provided, write to temporary file in `wt` mode. """
        self.temp = tempfile.NamedTemporaryFile(delete=False, mode='w')	#'wt' or 'w' so that we can write strings instead of bytes
        if contents:
            self.temp.write(contents)
        self.temp.close()	
    
    def __enter__(self):
        return self.temp.name
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.temp.close()
        os.remove(self.temp.name)
        

with make_file() as filename:
    open(filename, mode='wt').write('hello!')
    print(open(filename).read())

try:
    open(filename).read()
except FileNotFoundError as e:
    print(f'Raised {type(e).__name__}')


with make_file("hello!") as filename:
    print(open(filename).read())

with make_file(contents="hi!") as filename:
    print(open(filename).read())
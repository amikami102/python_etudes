# iospy.py
"""
A script of helper utilities for merging file-like streams and "spying" on stdout and stdin.
"""
from typing import *


class WriteSpy:
    """ A class that acts as a writable file stream that writes to two file-like objects at once. """
    
    def __init__(self, *files, close: bool = True):
        self.files = files
        self._close = close
        self._closed = False
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        for file in self.files:
            file.flush()
            if self._close:
                file.close()
            else:
                file.detach()
        self._closed = True
    
    def write(self, text: str):
        if self._closed:
            raise ValueError
        for file in self.files:
            file.write(text)
    
    def writable(self) -> tuple[bool]:
        if self._closed:
            raise ValueError
        return tuple(file.writable() for file in self.files)
    
    def close(self) -> bool:
        self._closed = True
    
    @property
    def closed(self) -> bool:
        return self._closed
    
    @closed.setter
    def closed(self, status: bool):
        self._closed = status
    

# base problem
f1 = open('file1.txt', mode='wt')
f2 = open('file2.txt', mode='wt')
with WriteSpy(f1, f2) as combined:
    print("Hello!", file=combined)
    combined.write(str(combined.writable()))

assert combined.closed
assert (f1.closed, f2.closed) == (True, True)
assert open('file1.txt').read(), open('file2.txt').read()\
    == ('Hello!\nTrue', 'Hello!\nTrue')

import sys
f1 = open('file1.txt', mode='wt')
with WriteSpy(sys.stdout, f1, close=False) as combined:
    print("Hello!", file=combined)
assert combined.closed
assert (f1.closed, sys.stdout.closed)
try:
    combined.writable()
except ValueError:
    print('passed')
else:
    print('failed')
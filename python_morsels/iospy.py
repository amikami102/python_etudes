# iospy.py
"""
A script of helper utilities for merging file-like streams and "spying" on stdout and stdin.
"""
from typing import *


class WriteSpy:
    """ A class that acts as a writable file stream that writes to two file-like objects at once. """
    
    def __init__(self, *files, close: bool = True):
        """
        files:	Iterable[io.TextIO]
            files to write into
        _close: bool, default True
            close the files if True, else do not close the files
        closed: bool
            indicates whether `WriteSpy` instance is closed
        """
        self.files: Iterable[io.TextIO] = files
        self._close = close
        self._closed = False
    
    def __enter__(self):
        return self
    
    def __exit__(self, type, value, traceback):
        self.close()
    
    def write(self, text: str):
        if self._closed:
            raise ValueError('File closed')
        for file in self.files:
            file.write(text)
    
    def writable(self) -> bool:
        """ Basically the opposite of `_closed` attribute value. """
        if self._closed:
            raise ValueError
        return True
    
    @property
    def closed(self) -> bool:
        return self._closed
    
    def close(self) -> None:
        """ Set `self._closed` to True. If `self._close` is True, close the files. """
        if self._close:
            for file in self.files:
                file.close()
        self._closed = True
    

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
assert (f1.closed, sys.stdout.closed) == (False, False)
try:
    combined.writable()
except ValueError:
    print('passed')
else:
    print('failed')
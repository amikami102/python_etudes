# file_looper.py
"""
A script defining a callable, `file_looper()`, which helps open many files in sequence.
"""
from typing import *


def file_looper(files, *args, return_exceptions: bool = False, **kwargs) -> Iterator[IO] | Exception:
    """
    Open `files` in sequence. If `return_exceptions` is True, return exceptions instead of raising them.
    """
    for file in files:
        try:
            yield open(file, *args, **kwargs)
        except Exception as e:
            if return_exceptions:
                yield e
            else:
                raise e



# base problem and bonus 1, which requires that files be opened lazily
filenames = ["file1.txt", "file2.txt", "file3.txt"]
n = 1
for f in file_looper(filenames, mode="w"):
    f.write(f"File {n}!")
    n += 1
for f in file_looper(filenames):
    print(f.read())



# bonus 2, test `return_exceptions` argument
import os
os.unlink('file2.txt')
for f in file_looper(filenames, return_exceptions=True):
    if isinstance(f, Exception):
        print(f)
    else:
        print(f.read())

for f in file_looper(filenames):
    print(f.read())
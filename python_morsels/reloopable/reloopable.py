# reloopable.py
"""
A script defining `reloopable` callable that lets you loop over a file.
"""
from typing import *

class reloopable:
    """Loop over a file-like object."""
    
    def __init__(self, file: TextIO):
        self.file = file
    
    def __iter__(self):
        self.file.seek(0)
        return self.file
    

# base problem
my_file = open('langston.txt')
lines = reloopable(my_file)
assert " ".join(lines).replace("\n", "").capitalize() ==\
    "Hold fast to dreams for when dreams go life is a barren field frozen with snow."
for line in lines:
    print(line)
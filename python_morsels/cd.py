# cd.py
"""
A script implementing a context manager class called `cd` that will change directories temporarily.
"""
import os
from pathlib import Path
from tempfile import TemporaryDirectory
from contextlib import contextmanager, nullcontext
from dataclasses import dataclass


@dataclass(frozen=True)
class Context:
    previous: os.PathLike
    current: os.PathLike


@contextmanager
def cd(directory: Path = None) -> None:
    previous = os.getcwd()
    cm = TemporaryDirectory() if directory is None else nullcontext(directory)
    with cm as directory:
        os.chdir(directory)
        try:
            yield Context(previous=previous, current=directory)
        finally:
            os.chdir(previous)
        

# base problem
subdir = Path('some_subdirectory')
subdir.mkdir(exist_ok=True)
(subdir/'my_file1.txt').write_text('hello world!')
with cd(subdir):
    print(Path('my_file1.txt').read_text())
    assert Path('my_file1.txt').is_file() == True
assert Path('my_file1.txt').is_file() == False

# bonus 1, test calling `cd()` with no argument
original = Path.cwd()
print(original.resolve())
with cd():
    print(Path.cwd())
    assert Path.cwd().resolve != original.resolve()
assert Path.cwd().resolve() == original.resolve()

# bonus 2, test `cd()` returns an object with `current` and `previous` attributes
with cd() as dirs:
    print('previous:', dirs.previous)
    print('current:', dirs.current)

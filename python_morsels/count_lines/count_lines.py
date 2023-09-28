# count_lines.py
"""
A script defining a function `count_lines()` that counts all the
lines in .py files within a given directory.
"""
from typing import *
import sys
from pathlib import Path
from dataclasses import dataclass, astuple
from collections import UserDict


class LineCounts(UserDict):
    """A dictionary-like object mapping file extensions to `Stat` objects."""
    def __init__(self) -> None:
        self.ignored = []
        super().__init__()


@dataclass
class Stat:
    files: int = 0
    lines: int = 0
    non_blank: int = 0
    
    def __iter__(self) -> Iterator[int]:
        yield from astuple(self)


def count_lines(
        directory: str, 
        extensions: list[str] = ('js', 'py', 'md', 'html')
    ) -> dict[str, Stat]:
    """
    Built a LineCounts() object by recursively looping through
    files and directories in `directory` that match extensions
    listed in `extensions`.
    """
    counts = LineCounts()
    allowed = {'js', 'py', 'md', 'html'}
    for ext in extensions:
        if ext in allowed:
            files, lines, non_blank = 0, 0, 0
            for path in Path(directory).rglob(f'*.{ext}'):
                try:
                    for line in path.open():
                        lines += 1
                        if line.strip() != '':
                            non_blank += 1
                except OSError as e:
                    LineCounts.append((path.name, e))
                    continue
                else:
                    files += 1
            if files:
                counts[ext] = Stat(files, lines, non_blank)
    return counts


# base problem
res = count_lines('two_files', {'py'})
assert set(res.keys()) == {'py'}
assert res['py'].files == 2 
assert res['py'].lines == 2 
assert res['py'].non_blank == 2
# test recursive 
res = count_lines('test_recursive')
assert set(res.keys()) == {'py'}
assert res['py'].files == 6
assert res['py'].lines == 15
assert res['py'].non_blank == 13

# bonus 1, test `extensions` argument
res = count_lines('test_extensions_arg')
assert set(res.keys()) == {'js', 'py', 'md', 'html'}
res2 = count_lines('test_extensions_arg', ['html', 'js', 'pyc'])
assert set(res2.keys()) == {'html', 'js'}

# bonus 2, test that unreadable files/directories are skipped over
# bonus 3, test `ignored` attribute on the dictionary-like object

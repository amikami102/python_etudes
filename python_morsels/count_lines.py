# count_lines.py
"""
A script defining a function `count_lines()` that counts all the lines within .py files in a given directory.
"""
from typing import *
import sys
from pathlib import Path
from dataclasses import dataclass, astuple
from collections import UserDict



@dataclass
class Stat:
    files: int = 0
    lines: int = 0
    non_blank: int = 0
    
    def __iter__(self) -> Iterator[int]:
        yield from astuple(self)


def count_lines(directories: Iterable[Path], extensions: list[str] = ['py', 'md', 'html', 'js']) -> dict[str, dict[str, int]]:
    """
    Return a dictionary whose keys are file extensions and values are their file and line counts.
    """
    
    unique_files = {
        path
        for ext in extensions
        for directory in directories
        for path in directory.rglob(f'*.{ext}')
    }
    for path in directories:
        # Path.rglob() does not return anything when the path object is a file even
        # if the patten matches
        if path.is_file() and path.suffix.lstrip('.') in extensions:
            unique_files.add(path)
    
    counts_dict: dict[str, Stat] = UserDict()
    for file in unique_files:
        stat = counts_dict.setdefault(file.suffix.lstrip('.'), Stat())
        stat.files += 1
        with open(file, 'r') as f:
            for line in f:
                stat.lines += 1
                if line.strip():
                    stat.non_blank += 1
    return counts_dict


def convert_to_list(counts_dict: dict[str, dict[str, int]]) -> list[tuple]:
    """Convert `counts_dict` into a list of tuples."""
    return sorted([(ext, *counts) for ext, counts in counts_dict.items()])


if __name__ == '__main__':
    print(
        count_lines(Path('toydir').glob(), extensions=['py', 'md', 'bin'])
    )

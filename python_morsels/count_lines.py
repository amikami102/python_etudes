# count_lines.py
"""
Count all the lines within .py files in a given directory recursively.

Usage example:
    $ mkdir toydir
    $ touch toydir/tau.py
    $ echo 'tau = 6.283185307179586\n' > toydir/tau.py
    $ touch toydir/helloworld.py
    $ echo 'print("hello world")' > helloworld.py
    $ touch toydir/file1.md
    $ echo 'This is the first line' >> toydir/file1.md
    $ echo 'This is the second line' >> toydir/file1.md
    $ echo '\n
    This is the fourth, but the third non-blank, line' >> toydir/file1.md
    $ python count_lines.py toydir
    
    
"""
from rich import print
import sys
import pathlib
from dataclasses import dataclass
import collections

@dataclass
class ContentStat:
    """
    A dataclass holding number of files
    and the number of lines, and number of non-blank lines in these files."""
    files: int	= 0		# number of .py files
    lines: int	= 0		# number of lines
    non_blank: int =0	# number of non-blank lines, i.e. non_blank <= lines


def count_lines(dir: str, extensions: list[str] = ['py', 'md', 'html', 'js']) -> dict[str, int]:
    """
    Return a dictionary with the name of the file extension without the period as the keys
    and ContentStat as values. Recursively search for all target files.
    
    Even though by default the function will search for files ending in 'py', 'md', 'html', or 'js',
    any file type that wasn't found in the directory should not be included in the output dictionary.
    """
    allowed: set[str] = {'py', 'md', 'html', 'js'}
    extensions: set[str] = set(extensions).intersection(allowed)
    out: dict[str, CountentStat]  = {}

    for file in pathlib.Path(dir).rglob('*'):
        if (key := file.suffix.lstrip('.')) in extensions:
            out.setdefault(key, ContentStat())
            out[key].files += 1
            with open(file, 'r') as f:
                for line in f:
                    out[key].lines += 1
                    if line.strip():
                        out[key].non_blank += 1
    return out

print(count_lines('toydir', extensions=['py', 'md', 'bin']))
# dups.py
"""
A program that accepts filenames and print groups of duplicate files found.

Usage example:
    $ python dups.py file1.txt file2.txt file3.txt file4.txt file5.txt file6.txt
    Duplicate group 1:
    file1.txt
    file3.txt
    file5.txt

    Duplicate group 2:
    file2.txt
    file4.txt
    
    $ python dups.py file1.txt file2.txt file6.txt
    No duplicate files found
    
    $ python dups.py dir1 dir2 file3.json readme.md
    Duplicate group 1:
    dir1/file1.txt
    dir2/file1_again.txt

    Duplicate group 2:
    dir1/file2.jpg
    dir1/subdir1/file2_again.JPG
    dir2/also_file2.jpeg

    Duplicate group 3:
    dir1/subdir/file3.json
    file3.json
    
    $ python dups.py --min-size=20 file1.txt file2.txt file3.txt file4.txt file5.txt file6.txt
    Duplicate group 1:
    file2.txt
    file4.txt
"""
from typing import Iterator
from find_duplicates import *
from pathlib import Path
import argparse


def get_files(files_or_dirs: list[Path], min_size: int) -> Iterator[Path]:
    for path in files_or_dirs:
        if path.is_file() and path.stat().st_size >= min_size:
            yield path
        if path.is_dir():
            yield from get_files(path.rglob(), min_size)


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('files', nargs='*', type=Path)
    parser.add_argument('--min-size', type=int, default=0)
    args = parser.parse_args()
    
    
    dupes = find_duplicates(get_files(args.files, args.min_size))
    if not dupes:
        print('No duplicate files found')
    else:
        for i, group in enumerate(dupes, start=1):
            print(f"Duplicate group {i}:", *group, sep='\n')
            
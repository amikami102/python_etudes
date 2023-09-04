# find_duplicates.py
"""
A scipt defining `find_duplicates()` functions which identifies duplicate files.
"""
from typing import *
from collections import defaultdict
import filecmp
import hashlib


def get_sha256_hash(filename: str) -> str:
    """ Calculate sha256 checksum of the content of `filename`. """
    with open(filename, mode='rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def find_duplicates(files: list[str]) -> Iterable[Iterable[str]]:
    """ Return an iterable of `files` grouped by sha256sum of file contents. """
    duplicates: dict = defaultdict(set)
    for file in files:
        file_sha56: str = get_sha256_hash(file)
        duplicates[file_sha56].add(file)
    return [
        group
        for group in duplicates.values()
        if len(group) > 1
    ]
    


# base problem, only test that the first file has any duplicates
assert find_duplicates(['file1.txt', 'file2.txt', 'file3.txt']) == [{'file1.txt', 'file2.txt'}]
assert find_duplicates(['file1.txt', 'file3.txt']) == []

# bonus 1, test pairwise comparison
assert find_duplicates(["file1.txt", "file2.txt", "file3.txt", "file4.txt"]) == [{'file2.txt', 'file1.txt'}, {'file4.txt', 'file3.txt'}]
# find_duplicates.py
"""
A scipt defining `find_duplicates()` functions which identifies duplicate files.
"""
from collections import defaultdict
import filecmp
import hashlib
from pathlib import Path


def get_sha256_hash(filepath: Path) -> str:
    """Calculate sha256 checksum of the content of `filename`."""
    return hashlib.sha256(filepath.read_bytes()).hexdigest()


def find_duplicates(files: list[str]) -> list[list[str]]:
    """Return an iterable of `files` grouped by sha256sum of file contents."""
    duplicates: dict[int, list[str]] = defaultdict(list)
    for file in files:
        file_sha56 = get_sha256_hash(file)
        if file not in set(duplicates[file_sha56]):
            duplicates[file_sha56].append(file)
    return [
        group
        for group in duplicates.values()
        if len(group) > 1
    ]
    

# remove_empty.py
"""
A program that removes empty directories recursively.
"""
from pathlib import Path
import sys


def remove_empty(directory: Path) -> None:
    """Remove empty directories recursively."""
    
    for subdir in directory.iterdir():
        if subdir.is_dir():
            remove_empty(subdir)
                
    if next(directory.iterdir(), None) is None:
        directory.rmdir()
        print(f'Deleting directory {directory.name}')
        

if __name__ == '__main__':
    remove_empty(Path(sys.argv[1]))
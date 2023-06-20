# cd.py
"""
A script implementing a context manager class called `cd` that will change directories temporarily.
"""
import os
import tempfile
from pathlib import Path

from rich import print


class cd:
    """Context manager for temporarily changing directories"""
    
    def __init__(self, directory: str | Path = None):
        """
        If `directory` is `None`, a temporary directory will be created.
        Do not switch directory yet.
        """
        self.directory = directory
        
    def __enter__(self):
        """
        Switch to `self.directory` or a temporary directory if `self.directory` is `None`.
        """
        
        self.current = Path().resolve()	# keep track of the original directory
        
        if not self.directory:	# create temporary directory
            self.temp = tempfile.TemporaryDirectory()
            os.chdir(self.temp.name)
        else:
            os.chdir(self.directory)
            
    def __exit__(self, exc_type, exc_value, exc_traceback):
        """
        Switch back to the original directory (`self.parent`).
        Delete the temporary directory if one was created.
        """
        os.chdir(self.current)	# switch back to the original directory
        if hasattr(self, 'temp'):	# remove temporary directory
            self.temp.cleanup()
        

# base problem
subdir = Path('some_subdirectory')
subdir.mkdir(exist_ok=True)
(subdir/'my_file.txt').write_text('hello world!')
with cd(subdir):
    print(Path('my_file.txt').read_text())
    assert Path('my_file.txt').is_file() == True
assert Path('my_file.txt').is_file() == False

# bonus 1
original = Path.cwd()
print(original.resolve())
with cd():
    print(Path.cwd())
    assert Path.cwd().resolve != original.resolve()
assert Path.cwd().resolve() == original.resolve()


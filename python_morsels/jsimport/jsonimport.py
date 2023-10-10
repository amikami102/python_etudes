# jsonimport.py
"""
A module for importing JSON files as modules.
"""
from pathlib import Path
import json
from typing import *
from importlib.machinery import ModuleSpec

T = TypeVar('T')
M = TypeVar('Module')


def import_json(name, paths) -> Optional[T]:
    """
    Find the first json file whose name is `text` from directories in `paths`
    and return the deserialized json object in the file.
    """
    for directory in paths:
        json_file = Path(directory) / f'{name}.json'
        if json_file.is_file():
            try:
                return json.loads(json_file.read_text())
            except json.JSONDecodeError as e:
                raise ImportError from e
    return None
        

# base problem
data = import_json('data', ['.'])
assert data['id'] == 1
assert data['plan']['name'] == 'pro'
data2 = import_json('data2', ['.'])
assert not data2


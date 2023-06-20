# Grouper.py
"""
A script defining `Grouper` class that accepts an iterable and a key function.
"""
from rich import print
from typing import *

T = TypeVar('T')
K = TypeVar('K')


class Grouper(Mapping[K, list[T]]):
    
    def __init__(self, iterable: Iterable[T] = None, key: Callable = None) -> None:
        self.key = keyfunc = key
        self.mapping = dct = {}
        if isinstance(iterable, Mapping):
            dct.update(iterable)
        elif not iterable:
            pass
        else:
            for item in iterable:
                dct.setdefault(keyfunc(item), [])
                dct[keyfunc(item)].append(item)
    
    def __getitem__(self, key: K) -> list[T]:
        """ Required by `Mapping`"""
        return self.mapping[key]
    
    def __iter__(self) -> Iterator[T]:
        """ Required by `Mapping`"""
        yield from self.mapping
        
    def __len__(self) -> int:
        """ Required by `Mapping`"""
        return len(self.mapping.keys())
    
    def update(self, items: Iterable) -> None:
        if isinstance(items, Mapping):
            for key, value in items.items():
                self.mapping.setdefault(key, []).extend(value)
        else:
            for item in items:
                self.mapping.setdefault(self.key(item), []).append(item)
        


# base problem
def first_letter(word: str) -> str:
    return word[0].upper()


sentence = 'Once upon a midnight dreary while I ponder weak and weary'
groups = Grouper(sentence.split(), key=first_letter)
assert groups['O'] == ['Once']
assert groups['W'] == ['while', 'weak', 'weary']
assert 'D' in groups
assert not 'N' in groups

groups = Grouper({1: ['a'], 4: ['once', 'upon']}, key=len)
assert groups[1] == ['a']

groups = Grouper(key=str.lower)
assert dict(groups) == {}

# bonus 1
groups = Grouper({1: ['a'], 4: ['once', 'upon']}, key=len)
groups.update({8: ['midnight'], 6: ['dreary']})
groups.update(['while', 'I', 'ponder', 'weak', 'and', 'weary'])
assert groups[4] == ['once', 'upon', 'weak']
assert groups[5] == ['while', 'weary']
assert groups[6] == ['dreary', 'ponder']


words = ["Apple", "animal", "apple", "ANIMAL", "animal"]
word_groups = {
    "apple": ["Apple", "apple", "APPLE", "APPLE"],
    "animal": ["animal", "ANIMAL", "animal"],
    "lemon": ["lemon", "Lemon", "lemon", "LEMON"],
    "orange": ["Orange"],
}
more_items = {
    "apple": ["APPLE"],
    "lemon": ["lemon", "LEMON"],
    "orange": ["Orange"],
}
groups = Grouper(words, key=str.lower)
groups.update(["lemon", "Lemon", "APPLE"])
groups.update(more_items)
assert dict(groups) == word_groups
# Grouper.py
"""
A script defining `Grouper` class that accepts an iterable and a key function.
"""
from typing import *


class Grouper(MutableMapping):
    """A dictionary-like class that groups items."""
    
    def __init__(self, iterable: Iterable = (), *, key: Callable = None):
        self.groups = {}
        self.keyfunc = key
        self.update(iterable)

    def __len__(self) -> int:
        return sum(1 for _ in self.groups)

    def __iter__(self) -> Iterator[Hashable]:
        yield from self.groups

    def __getitem__(self, key: Hashable) -> Any:
        return self.groups[key]
    
    def __setitem__(self, key: Hashable, value: Any):
        self.groups[key] = value
    
    def __delitem__(self, key: Hashable) -> None:
        del self.groups[key]
    
    def update(self, mapping: Mapping) -> None:
        if isinstance(mapping, Mapping):
            for value in mapping.values():
                key = self.keyfunc(value[0])
                self.groups.setdefault(key, []).extend(value)
        else:
            for item in mapping:
                key = self.keyfunc(item)
                self.groups.setdefault(key, []).append(item)
    
    def add(self, item) -> None:
        key = self.keyfunc(item)
        self.groups.setdefault(key, []).append(item)
    
    def group_for(self, item) -> Hashable:
        return self.keyfunc(item)
    
    def __add__(self, other: 'Grouper') -> 'Grouper':
        if not isinstance(other, type(self)):
            return NotImplemented
        elif self.keyfunc != other.keyfunc:
            raise ValueError(
                "The Grouper objects do not have the same key function"
            )
        else:
            added = Grouper(self, key=self.keyfunc)
            added.update(other.groups)
            return added


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
more_items = {
    "apple": ["APPLE"],
    "lemon": ["lemon", "LEMON"],
    "orange": ["Orange"],
}
groups = Grouper(words, key=str.lower)
groups.update(["lemon", "Lemon", "APPLE"])
groups.update(more_items)
assert dict(groups) == {
    "apple": ["Apple", "apple", "APPLE", "APPLE"],
    "animal": ["animal", "ANIMAL", "animal"],
    "lemon": ["lemon", "Lemon", "lemon", "LEMON"],
    "orange": ["Orange"],
}

# bonus 2, test `add()` and `group_for()` methods
groups = Grouper(key=len)
groups.add('once')
assert groups.group_for('upon') == 4
assert groups.group_for('a') == 1
assert groups[4] == ['once']

# bonus 3, test that `Grouper` objects can be concactenated
words1 = Grouper("You say goodbye and I say hello".split(), key=str.lower)
words2 = Grouper("Hello hello".split(), key=str.lower)
merged = words1 + words2
assert merged['hello'] == ['hello', 'Hello', 'hello']
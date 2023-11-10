# HistoryDict.py
"""A dictionary-like class that keeps track of previous values for keys."""
from typing import *
from collections import defaultdict


class _DeletedValue:
    def __repr__(self):
        return 'DELETED'

DELETED = _DeletedValue()


class HistoryDictView(Mapping):
    
    def __init__(self, historydict: MutableMapping):
        self._mapping = dict(historydict)
    def __getitem__(self, key):
        return HistoryView(self._mapping[key])
    def __len__(self):
        return sum(1 for _ in self._mapping)
    def __iter__(self):
        return (key for key, value in self._mapping if value)


class HistoryView:
    def __init__(self, history: list):
        self.history = history
    def __iter__(self):
        yield from self.history
    def __setitem__(self, index, value):
        raise TypeError
    def __getitem__(self, index):
        return self.history[index]
    


class HistoryDict(MutableMapping):
    """A dictionary-like class that keeps a history of values."""
    
    def __init__(self, mapping: dict|list[tuple] = ()):
        self.current = {}
        self.previous = defaultdict(list)
        self.update(mapping)
    
    def __getitem__(self, key: str) -> Any:
        return self.current[key]
    
    def __setitem__(self, key: str, value: Any):
        self.current[key] = value
        self.previous[key].append(value)
    
    def __delitem__(self, key: str):
        del self.current[key]
        self.previous[key].append(DELETED)
    
    def __iter__(self) -> Iterator:
        yield from self.current
    
    def __len__(self) -> int:
        return len(self.current)
    
    def __repr__(self) -> str:
        return f'{type(self).__name__}({self.current})'
    
    def history(self, key: str) -> HistoryView:
        return HistoryView(self.previous[key])
    
    def all_history(self) -> HistoryDictView:
        return HistoryDictView(self.previous)


# base problem
things = HistoryDict({"ducks": 3, "stickers": 10})
things2 = HistoryDict([("ducks", 3), ("stickers", 10)])
things3 = HistoryDict()

things2['stickers'] = 5
things3.update({'ducks': 3, 'stickers': 10})

assert str(things) == "HistoryDict({'ducks': 3, 'stickers': 10})"
assert list(things2.history('ducks')) == [3]
assert list(things2.history('stickers')) == [10, 5]
things3.setdefault("ducks", 20)
things3.setdefault('laptops', 1)
assert list(things3.history('ducks')) == [3]
assert list(things3.history('laptops')) == [1]

assert things != things2
assert things != things3
assert things3.pop('laptops') == 1
assert things == things3
things4 = HistoryDict({"ducks": 3, "stickers": 10})
assert things4 == things3
assert things == {"ducks": 3, "stickers": 10}


# bonus 1, test key deletion
things4 = HistoryDict({'ducks': 4})
del things4['ducks']
assert list(things4.history('ducks')) == [4, DELETED]
assert repr(DELETED) == 'DELETED'

# bonus 2, test calling `history()` on unknown keys
# and `all_history()` method
assert list(things.history('apples')) == []
things5 = HistoryDict({"ducks": 9, "stickers": 6})
past = things5.all_history()
assert list(past['ducks']) == [9]
assert list(past['stickers']) == [6]
things5.pop('stickers')
things5['stickers'] = 10
things5['ducks'] = 1
past = things5.all_history()
assert list(past['ducks']) == [9, 1]
assert list(past['stickers']) == [6, DELETED, 10]

# bonus 3, test that `history()` and `all_history()` return dictionary views
things6 = HistoryDict({"ducks": 9, "stickers": 6})
ducks_history = things6.history("ducks")
try:
    ducks_history[0] = 1
except TypeError:
    print('passed')
else:
    print('failed')
all_history = things6.all_history()
try:
    del all_history["ducks"]
except TypeError:
    print('passed')
else:
    print('failed')
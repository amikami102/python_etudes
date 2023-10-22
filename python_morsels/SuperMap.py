# SuperMap.py
"""
A script defining a class, `SuperMap`, that keeps track of hashable objects
based on attributes.
"""
from typing import *
from collections import defaultdict
from functools import cached_property


class SuperMap(MutableSet):
    """Keeps track of hashables objects based on specific attributes."""
    
    def __init__(self, objects: Iterable = (), indexes: Iterable[str] = ()):
        self.objects = set(objects)
        self.indexes = defaultdict(lambda: defaultdict(set))
        for obj in self.objects:
            for index in self.indexes:
                value = getattr(obj, index)
                self.indexes[index][value].add(obj)
    
    def where(self, **kwargs):
        if unindexed := (kwargs.keys() - self.indexes.keys()):
            raise ValueError(f'Attribute not indexed: {", ".join(unindexed)}')
        return set.intersection(
            *(self.mapping[key][value] for key, value in kwargs.items())
        )
    
    def __iter__(self):
        yield from self.objects
    
    def __repr__(self):
        return f'{type(self).__name__}({self.objects!r})'
    
    def __len__(self):
        return len(self.objects)
    
    def __contains__(self, obj):
        return obj in self.objects
    
    def add(self, obj):
        self.objects.add(obj)
    
    def discard(self, obj):
        self.objects.discard(obj)
    
    def update(self, objects):
        self.objects.update(objects)


# base problem
from typing import NamedTuple

class Person(NamedTuple):
    name: str
    joined: int
    hat_color: str = "purple"
    active: bool = True
    
person_list = [
    Person(name="Guido", joined=2019, active=False, hat_color="yellow"),
    Person(name="Carol", joined=2019, hat_color="blue"),
    Person(name="Brett", joined=2019, hat_color="purple"),
    Person(name="Barry", joined=2019, hat_color="pink"),
    Person(name="Thomas", joined=2020, hat_color="purple"),
]
people = SuperMap(person_list, indexes=['joined', 'active', 'hat_color'])

assert [*people.where(hat_color='black')] == []
assert [*people.where(hat_color='yellow')] ==\
    [Person(name='Guido', joined=2019, hat_color='yellow', active=False)]

# bonus 1
assert len(people) == 5
assert {person.name for person in people.where(active=True, joined=2019)} ==\
    {'Carol', 'Barry', 'Brett'}
try:
    people.where(id=4)
except ValueError:
    print('passed')
    
# bonus 2,
for person in people.where(active=False):
    people.discard(person)
assert list(people.where(active=False)) == []
people.add(Person(name="Terry", joined=1969, active=True))
assert [p.name for p in people.where(joined=1969)] == ['Terry']
people.update([Person(name="John", joined=1969), Person(name="Eric", joined=1969)])
assert {p.name for p in people.where(joined=1969)} ==\
    {'Eric', 'John', 'Terry'}

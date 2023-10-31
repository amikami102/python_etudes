# QueryList.py
from typing import *
from collections import UserList
import operator
from functools import partial

DataObject = TypeVar('data object')
T = TypeVar('T')
OPERATORS = {
    'gt': operator.gt,
    'lt': operator.lt,
    'ne': operator.ne,
    'contains': operator.contains,
    'in': lambda x, y: operator.contains(y, x)
}


def matches(obj: DataObject, query: str, value: T) -> bool:
    """Return True if `obj` matches `query` for `value`."""
    field, _, operator_type = query.partition('__')
    operation = OPERATORS.get(operator_type, operator.eq)
    return operation(getattr(obj, field), value)


def attrs_match(obj: DataObject, queries: list[tuple[str, T]]) -> bool:
    """Return True if all `queries` match for `obj`."""
    return all(
        matches(obj, query, value)
        for query, value in queries
    )


class QueryList(UserList):
    """Supports queries on a given list of items based on their attributes."""
    
    def filter(self, *f_queries: tuple[str, T], **queries: Mapping) -> 'QueryList':
        queries: list[tuple[str, T]] = [*f_queries, *queries.items()]
        return QueryList(
            obj for obj in self.data
            if attrs_match(obj, queries)
        )
    
    def attrs(self, *names) -> list:
        getter = operator.attrgetter(*names)
        return [getter(obj) for obj in self.data]


class Field:
    def __getattr__(self, name) -> 'Lookup':
        return Lookup(name)
    
    
F = Field()


class Lookup:
    def __init__(self, name):
        self.name = name
        
    def make_query(self, op: str, value: T) -> tuple[str, T]:
        return f'{self.name}__{op}', value
    
    def __eq__(self, value): return self.make_query('eq', value)
    def __ne__(self, value): return self.make_query('ne', value)
    def __lt__(self, value): return self.make_query('lt', value)
    def __gt__(self, value): return self.make_query('gt', value)
    def __contains__(self, value): return self.make_query('contains', value)
    

# base problem
class Location(NamedTuple):
    name: str
    x: float
    y: float

places = [
    Location("home", 0, 0),
    Location("work", 2, 2),
    Location("park", -2, 2),
    Location("store", 2, -2),
]

query = QueryList(places)
assert sorted(place.name for place in query.filter(y=2)) == ['park', 'work']
assert [place.name for place in query.filter(x=2, y=2)] == ['work']
query.append(Location("lake", 2, 6))
assert sorted(place.name for place in query.filter(x=2)) ==\
       ['lake', 'store', 'work']
assert sorted(query.filter(x=2).attrs("name")) == ['lake', 'store', 'work']
assert sorted(query.filter(x=2).attrs("name", 'y')) ==\
    [('lake', 6), ('store', -2), ('work', 2)]
assert query.filter().attrs("name") == ['home', 'work', 'park', 'store', 'lake']

# bonus 1, test filter operations
assert query.filter(y__gt=0).attrs("name") == ['work', 'park', 'lake']
assert query.filter(y__gt=0, y__ne=2).attrs("name") == ['lake']
assert query.filter(y__gt=0, y__ne=2, x__in=[0, 1]).attrs("name") == []

# bonus 2, test filter operations with `F` object
assert query.filter(F.x == 2).attrs("name", 'y') ==\
    [('work', 2), ('store', -2), ('lake', 6)]
assert query.filter(F.x > 0, F.y != 2).attrs("name") == ['store', 'lake']


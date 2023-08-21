# pluck.py
"""
A script defining function `pluck()`, which looks up keys in nested dictionaries.
"""
from typing import *

T = TypeVar('T')
SENTINEL = object()


def single_pluck(nested_dict: dict[dict], path: str, sep: str, default: T) -> T:
    """
    Return the value at the `sep`-concatenated string path, `path`, of `nested_dict`.
    If `default` is not None, return `default` argument if the key does not exist;
    otherwise raise KeyError.
    """
    if not path:
        # we've reached the destination of the path
        return nested_dict
    
    key_iterator = iter(path.split(sep))
    try:
        value = nested_dict[next(key_iterator)]
    except KeyError:
        if default is not SENTINEL:
            return default
        else:
            raise 
    else:
        return single_pluck(value, sep.join(key_iterator), sep, default)


def pluck(nested_dict: dict, *paths, sep: str = '.', default: T = SENTINEL) -> tuple[T]:
    """
    Return the tuple of outputs found by `single_pluck`-ing all the `paths` on `nested_dict`.
    """
    if len(paths) == 1:
        # if there is only one string path, return the value at the path
        return single_pluck(nested_dict, *paths, sep, default)
    return tuple(single_pluck(nested_dict, path, sep, default) for path in paths)
    

# base problem
data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
assert pluck(data, 'amount') == 10.64
assert pluck(data, 'category.group') == 'Fun'
try:
    pluck(data, 'category.created')
except KeyError:
    print('passed')
else:
    print('failed')
    
example = {'1': {'a': {'i': 9, 'ii': 8}, 'b': 7}, '2': 6}
assert example['1']['a']['ii'] == pluck(example, '1.a.ii')

# bonus 1, test `sep` argument
data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
assert pluck(data, 'category/name', sep='/') == 'Music'

# bonus 2, test `default` argument
data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
assert pluck(data, 'category.created', default='N/A') == 'N/A'
d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}
assert pluck(d, 'c.e', default=None) is None

# bonus 3, test any number of `paths` arguments
data = {'amount': 10.64, 'category': {'name': 'Music', 'group': 'Fun'}}
assert pluck(data, 'category.name', 'amount') == ('Music', 10.64)
# jsonify.py
"""
A script defining `jsonify` function decorator that will return a JSON-encoded version of the decorated function.
"""
from typing import *
import json
from functools import wraps

def jsonify(func: Callable) -> Callable:
    """Json-ify the return value of `func`."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        return json.dumps(return_value)
    return wrapper


# base problem
@jsonify
def make_user(id: Any, options: Optional[Any]) -> dict:
    return {'id': id, 'live': False, 'options': options}
assert make_user(4, options=None) == '{"id": 4, "live": false, "options": null}'
print(make_user)
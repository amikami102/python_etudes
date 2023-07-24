# FieldTracker.py
"""
A script defining `FieldTracker` class that tracks which attributes have changed on a class.
"""
from typing import *

T = TypeVar('T')

class FieldTracker:
    """
    Tracks whether attributes of child classes have changed.
    Assume that
            - child classes will always call `super().__init__()` after setting attribute values;
            - child classes will reset field in their `save()` method and will call `super().save()` if they override save.
    
    Methods:
    -------
        previous(field: str) -> T
            Returns the previous value of `field` if the field value has changed; otherwise return the current value
            
        has_changed(field: str) -> bool
            Returns whether `field` has changed value since the class instance was created.
            
        changed(None) -> dict[str, T]
            Returns a dictionary of child class fileds and their previous values
    """
    def __init__(self, **kwargs):
        self._tracked = {
            field: getattr(self, field)
            for field in type(self).fields
        }
        print(self._tracked)
    
    def save(self):
        self._tracked.update(
            {field: getattr(self, field) for field in self.fields}
        )
    
    def previous(self, field: str) -> T:
        """ Return `field`'s value stored in `_tracked` attribute. """
        return self._tracked[field]
    
    def has_changed(self, field: str) -> bool:
        """ Return True if current value of `field` is different from its tracked value. """
        return getattr(self, field) != self._tracked[field]
    
    def changed(self) -> dict[str, T]:
        """ Return a dictionary of field and their previous values of fields whose values have changed. """
        return {
            field: self._tracked[field]
            for field in self.fields
            if self.has_changed(field)
        }


class FieldTrackerMixin(FieldTracker):
    """ Works like a `FieldTracker` but can be used to track attributes of another parent class. """
    


# base problem
class Point(FieldTracker):
    fields = ('x', 'y', 'z')
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        super().__init__()
    def save(self):
        # Do something in a database or something
        print("Point saved!", self.x, self.y, self.z)
        super().save()

p = Point(1, 2, 3)
assert p.previous('x') == 1
assert not p.has_changed('x')
assert not p.changed()
p.x = 0
assert p.previous('x') == 1
assert p.has_changed('x')
assert p.changed() == {'x': 1}

# bonus 1 test `FieldTrackerMixin` class
class Model:
    def __init__(self, **kwargs):
        assert set(kwargs.keys()) == set(self.attrs)
        for name, value in kwargs.items():
            setattr(self, name, value)
    def save(self):
        print("Saving...")
        for name, value in self.changed().items():
            print("Changed:", name, "=", value)
        print("Saved.")

class Point(FieldTrackerMixin, Model):
    fields = attrs = ('x', 'y', 'z')

p = Point(x=1, y=2, z=3)
p.x = 0
assert p.changed() == {'x': 1}
p.save()
assert p.changed() == {}

# alias.py
"""
A script defining `alias`, a descriptor that makes aliases for class attributes.
"""
class alias:
    """A descriptor that makes aliases for attributes."""
    def __init__(self, attribute: str, *, write: bool = False):
        self.attribute = attribute
        self.write = write
        
    def __get__(self, obj, objtype=None):
        return getattr(obj, self.attribute)
    
    def __set__(self, obj, value) -> None:
        if not self.write:
            raise AttributeError
        setattr(obj, self.attribute, value)


# base problem
class DataRecord:
    title = alias('serial')
    def __init__(self, serial):
        self.serial = serial

record = DataRecord("148P")
assert record.title == '148P'
assert record.serial == '148P'
record.serial = '148X'
assert record.title == '148X'

# bonus 1, test alias assignment
class DataRecord:
    title = alias('serial')
    def __init__(self, serial):
        self.serial = serial

record = DataRecord("148X")
try:
    record.title = "149S"
except AttributeError:
    print('passed assignment to alias attribute')
else:
    print('failed')

# bonus 2, accept `write` keyword argument
class DataRecord:
    title = alias('serial', write=True)
    def __init__(self, serial):
        self.serial = serial

record = DataRecord("192B")
record.title = "192A"
assert record.serial == '192A'
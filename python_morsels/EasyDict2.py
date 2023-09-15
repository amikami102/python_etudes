# EasyDict2.py
"""
A script defining `EasyDict` class.
"""
from collections import UserDict


class EasyDict(UserDict):
    
    __slots__ = ('data',)	# remove `__dict__` attribute
    
    def __getattr__(self, name):
        try:
            return self.data[name]
        except KeyError:
            raise AttributeError
  
    def __setattr__(self, name, value):
        if name in self.__slots__:
            return super().__setattr__(name, value)
        self.data[name] = value

    
# base problem
person = EasyDict({'name': 'Kamado Tanjiro', 'location': 'Tokyo', 'era': 'Taisei'})
assert person.name == 'Kamado Tanjiro'
assert person['location'] == 'Tokyo'
person.location = 'Kyoto'
assert person['location'] == 'Kyoto'
person = EasyDict(name="Kamado Tanjiro", location='Tokyo', era='Taisho')
assert person.location == 'Tokyo'
assert person != EasyDict(name="Kamado Tanjiro", location="Tokyo")
assert person == EasyDict(name="Kamado Tanjiro", location="Tokyo", era='Taisho')
assert not person.get('profession')
assert person.get('profession', 'unknown') == 'unknown'
assert person.get('name', 'unknown') == 'Kamado Tanjiro'

# bonus 1
person = EasyDict(name="竈門禰󠄀豆子", location="刀鍛冶の里")
assert list(person.keys()) == ['name', 'location']
assert list(person.values()) == ["竈門禰󠄀豆子", "刀鍛冶の里"]
assert list(person.items()) == [('name', '竈門禰󠄀豆子'), ('location', '刀鍛冶の里')]
assert person.pop("name", "") == "竈門禰󠄀豆子"
assert person.pop("name", "") == ''
person = EasyDict(name="時透無一郎", location="刀鍛冶の里")
assert len(person) == 2
assert "name" in person
assert "age" not in person
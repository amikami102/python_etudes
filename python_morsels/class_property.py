# class_property.py
"""
A script defining
    - `class_property` decorator,
        which is a combination of `property` and `classmethod` decorators;
    - `class_only_property` decorator,
        which works like `class_property` but raises error if accessed on class instance.
"""
from typing import *


class class_property:
    """ A decorator that acts like `property` and `classmethod` decorators combined. """
    def __init__(self, getter: Callable):
        self.getter = getter
    
    def __get__(self, obj: Any, obj_type: type = None):
        if not obj:
            return self.getter(obj_type)
        else:
            return self.getter(type(obj))

    
class class_only_property:
    """ Like `class_property` but only access attributes at class level. """
    def __init__(self, getter: Callable):
        self.getter = getter
    
    def __get__(self, obj, obj_type = None):
        if obj and not obj_type:
            raise AttributeError('Cannot be accssed on class instances')
        return self.getter(obj_type)


# base problem
class BankAccount:
    accounts = []
    def __init__(self, balance=0):
        self.balance = balance
        self.accounts.append(self)
    
    @class_property
    def total_balance(cls):
        return sum(a.balance for a in cls.accounts)

assert BankAccount.total_balance == 0
account1 = BankAccount(balance=95)
account2 = BankAccount(balance=53)
assert BankAccount.total_balance == 148
assert account1.balance == 95
assert account1.total_balance == BankAccount.total_balance == 148

class Thing:
    @class_property
    def stuff(cls):
        assert cls is Thing
        return cls
assert Thing.stuff is Thing
assert Thing().stuff is Thing

# bonus 1, test `class_only_property`
from contextlib import suppress
class BankAccount:
    accounts = []
    def __init__(self, balance=0):
        self.balance = balance
        self.accounts.append(self)
    @class_only_property
    def total_balance(cls):
        return sum(a.balance for a in cls.accounts)

assert BankAccount.total_balance == 0
account1 = BankAccount(balance=95)
account2 = BankAccount(balance=53)
assert BankAccount.total_balance == 148
assert account1.balance == 95
with suppress(AttributeError):
    account1.total_balance
    
# bonus 2, make `class_only_property` allow attributes of the same name on class instances
# (my solution passed bonus 2 when it passed bonus 1)
class BankAccount:
    accounts = []
    def __init__(self, balance=0):
        self.balance = balance
        self.accounts.append(self)
    @class_only_property
    def balance(cls):
        return sum(a.balance for a in cls.accounts)

assert BankAccount.balance == 0
account1 = BankAccount(balance=95)
account2 = BankAccount(balance=53)
assert BankAccount.balance == 148
assert account1.balance == 95
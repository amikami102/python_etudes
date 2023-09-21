# PhoneNumber.py
"""
A script defining `PhoneNumber`, a class that represents a US-style
phone number.
"""
from typing import Iterator
import re
from dataclasses import dataclass, field, InitVar, astuple

US_NUMBER_RE = re.compile("""
    ^			# start of string
    \W?			# optional non-word characters like '('
    (\d{3})		# area code (captured)
    \W?			# optional non-word characters like ')'
    \W{,3}		# up to 3 non-word characters like ' - '
    (\d{3})		# prefix (captured)
    \W{,3}		# up to 3 non-word characters like ' - '
    (\d{4})		# line number (captured)
    $			# end of string
""", re.VERBOSE)


@dataclass(eq=True, frozen=True)
class PhoneNumber:
    """A US phone number."""
    number: InitVar[str]
    area_code: str = field(init=False)
    prefix: str = field(init=False)
    line_number: str = field(init=False)
    
    
    def __post_init__(self, number: str):
        if match := US_NUMBER_RE.match(number):
            area_code, prefix, line_number = match.groups()
            super().__setattr__('area_code', area_code)
            super().__setattr__('prefix', prefix)
            super().__setattr__('line_number', line_number)
        else:
            raise ValueError
    
    def __repr__(self) -> str:
        number = f"{self.area_code}{self.prefix}{self.line_number}"
        return f"{type(self).__name__}({number!r})"

    def __str__(self) -> str:
        return f"{self.area_code}-{self.prefix}-{self.line_number}"

    def __format__(self, fmt: str) -> str:
        match fmt:
            case '(':
                return f"({self.area_code}) {self.prefix}-{self.line_number}"
            case single_sep if single_sep in {'-', ' ', '.'}:
                return single_sep.join(iter(self))
            case sep if sep in {'- ', '. '}:
                sep = ' ' + sep
                return sep.join(astuple(self))
            case '+':
                return '+1' + ''.join(astuple(self))
            case '+ ':
                return '+1 ' + ' '.join(astuple(self))
            case '':
                return str(self)


# base problem
whitehouse = PhoneNumber('(202) 456-1414')
assert whitehouse.prefix == '456'
assert whitehouse.area_code == '202'
assert whitehouse.line_number == '1414'
assert repr(whitehouse) == "PhoneNumber('2024561414')"
assert str(whitehouse) == "202-456-1414"
the_president = PhoneNumber('202.456.1111')
givewell = PhoneNumber('415 - 689 - 5803')
give_directly = PhoneNumber('6465044837')

# bonus 1, test that ValueError is raised
try:
    PhoneNumber("My number is 716-776-2323")
except ValueError:
    print('passed')
try:
    PhoneNumber("212a664b7665")
except ValueError:
    print('passed')
try:
    PhoneNumber("21 26 64 76 65")
except ValueError as e:
    print('passed')

# bonus 2, test equality, immutability, and hashability
whitehouse = PhoneNumber('(202) 456-1111')
the_president = PhoneNumber('202.456.1111')
assert whitehouse == the_president
numbers = {whitehouse}
assert whitehouse in numbers
try:
    whitehouse.area_code = 808
except AttributeError:
    print('passed immutability')

# bonus 3, test customized string formatting
phone = PhoneNumber('(202) 456-1111')
assert f"Call {phone:(}" == "Call (202) 456-1111"
assert f"Call {phone:-}" == "Call 202-456-1111"
assert f"Call {phone: }" == "Call 202 456 1111"
assert f"Call {phone:.}" == "Call 202.456.1111"
assert f"Call {phone:- }" == "Call 202 - 456 - 1111"
assert f"Call {phone:. }" == "Call 202 . 456 . 1111"
assert f"Call {phone:+ }" == "Call +1 202 456 1111"
assert f"Call {phone:+}" == "Call +12024561111"
assert f"Call {phone}" == "Call 202-456-1111"
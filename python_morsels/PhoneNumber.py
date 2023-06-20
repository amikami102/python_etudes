# PhoneNumber.py
"""
A script defining `PhoneNumber`, a class that represents a US-style phone number.
"""
import re

from rich import print


valid_format = re.compile(r"""^
[(]{0,1}[0-9]{3}[)]{0,1} # area code
(((\s\W\s){0,1})|[-\s\.]{0,1}) # separator
[0-9]{3} # prefix
(((\s\W\s){0,1})|[-\s\.]{0,1}) # separator
[0-9]{4}  # line number
$""",
re.X)

class PhoneNumber:
    """
    A class object that holds US-style phone number.
    The phone number is checked that it is a US phone number during class instantiation.

    This object is immutable and hashable.

    Attributes
    ----------
        area_code: str
            the first three digits
        prefix: str
            the next 3 digits following the area code
        line_number: str
            the last 4 digits
    """


    def __init__(self, phone_number: str):
        if not re.match(valid_format, phone_number):
            raise ValueError('Invalid phone number')
        numbers: list[str] = [p for p in phone_number if p.isdigit()]
        super().__setattr__('area_code', ''.join(numbers[:3]))
        super().__setattr__('prefix', ''.join(numbers[3:6]))
        super().__setattr__('line_number', ''.join(numbers[6:]))

    def __str__(self) -> str:
        return '-'.join(
            (self.area_code, self.prefix, self.line_number)
            )

    def __repr__(self) -> str:
        phone_number = ''.join(
            (self.area_code, self.prefix, self.line_number)
            )
        return f'{type(self).__name__}({phone_number!r})'

    def __eq__(self, other: 'PhoneNumber') -> bool:
        if not isinstance(other, PhoneNumber):
            return NotImplemented
        return self.area_code == other.area_code and\
            self.prefix == other.prefix and\
            self.line_number == other.line_number

    def __setattr__(self, key, value):
        raise AttributeError('PhoneNumber cannot be modified.')

    def __hash__(self):
        return hash(str(self))


if __name__ == '__main__':

    # Base problem
    whitehouse = PhoneNumber('(202) 456-1414')
    print(whitehouse.prefix)
    print(whitehouse.area_code)
    print(whitehouse.line_number)
    print(repr(whitehouse))
    print(whitehouse)

    the_president = PhoneNumber('202.456.1111')
    givewell = PhoneNumber('415 - 689 - 5803')
    give_directly = PhoneNumber('6465044837')
    print(the_president, givewell, give_directly)

    # Bonus 1
    try:
        PhoneNumber("My number is 716-776-2323")
    except ValueError as e:
        print('Invalid due to incorrect string value')

    try:
        PhoneNumber("88-716-776-2323")
    except ValueError as e:
        print('Invalid due to extra numbers')

    try:
        PhoneNumber("21 26 64 76 65")
    except ValueError as e:
        print('Invalid due to invalid grouping')

    # Bonus 2
    del whitehouse
    del the_president
    whitehouse = PhoneNumber('(202) 456-1111')
    the_president = PhoneNumber('202.456.1111')
    print(whitehouse == the_president)
    print(hash(whitehouse))
    numbers = {whitehouse}
    print(whitehouse in numbers)
    

# format_bytes.py
"""
A script defining `format_bytes()`, which formats an integer into a human-readable byte size.
"""
import re

from rich import print

KILO: int = 1_000
KIBI: int = 1_024

INT_BYTES: dict[int, str] = {
    KILO ** 4: 'TB',
    KILO ** 3: 'GB',
    KILO ** 2: 'MB',
    KILO ** 1: 'KB',
    KILO ** 0: 'B'
}
INT_BITS: dict[int, str] = {
    k: unit.replace('B', 'b')
    for k, unit in INT_BYTES.items()
}
INT_BINARY: dict[int, str] = {
    KIBI ** 4: 'TiB',
    KIBI ** 3: 'GiB',
    KIBI ** 2: 'MiB',
    KIBI ** 1: 'KiB',
    KIBI ** 0: 'B'
}
BYTES_RE = re.compile("([0-9]{1,3})(.+)")


def format_bytes(my_bytes: int, bits: bool = False, binary: bool = False) -> str:
    """
    Return a string representing `my_bytes` as a string with 1-3 digits and unit of measurement.
    If `bits` is True, measure `my_bytes` in unit of bits.
    If `binary` is True, return the binary equivalents. 
    """
    if my_bytes < 0:
        raise ValueError('`my_bytes` must not be negative')
    
    if bits:
        conversion: dict[int, str] = INT_BITS
        my_bytes *= 8	# there are 8 bits in 1 byte
    elif binary:
        conversion = INT_BINARY
    else:
        conversion = INT_BYTES
        
    for size, unit in conversion.items():
        q, _ = divmod(my_bytes, size)
        if q:
            return f'{round(my_bytes / size):d}{unit}'
    
    return f'{my_bytes}{unit}'


def parse_bytes(string: str) -> int:
    """ Reverse `format_bytes()` and return the bytes in integer."""
    digits, unit = BYTES_RE.match(string).groups()
    bits: bool = False	# flag to indicate that the input is bits
    
    if unit == 'B':
        return int(digits)
    elif 'i' in unit:
        conversion = {v: k for k, v in INT_BINARY.items()}
    elif 'b' in unit:
        conversion = {v: k for k, v in INT_BITS.items()}
        bits = True
    else:
        conversion = {v: k for k, v in INT_BYTES.items()}
    
    return conversion[unit] * int(digits)//8 if bits else \
        conversion[unit] * int(digits)
        
        
    
    

# base problem, test the vanilla version of `format_bytes()`
assert format_bytes(0) == '0B'
assert format_bytes(500) == '500B'
assert format_bytes(56374) == '56KB'
assert format_bytes(87238722) == '87MB'
assert format_bytes(9876543210) == '10GB'
assert format_bytes(591627861221937) == '592TB'

# bonus 1, test the optional `bits` argument
assert format_bytes(0, bits=True) == '0b'
assert format_bytes(500, bits=True) == '4Kb'
assert format_bytes(500, bits=False)== '500B'
assert format_bytes(56374, bits=True) == '451Kb'
assert format_bytes(9876543210, bits=True) == '79Gb'

# bonus 2, test the optional `binary` argument
assert format_bytes(500, binary=True) == '500B'
assert format_bytes(56374, binary=True) == '55KiB'
assert format_bytes(87238722, binary=True) == '83MiB'
assert format_bytes(87238722, binary=False) == '87MB'
assert format_bytes(9876543210, binary=True) == '9GiB'
assert format_bytes(591627861221937, binary=True) == '538TiB'

# bonus 3, test `parse_bytes()` function
assert parse_bytes('56KB') == 56_000
assert parse_bytes('30Mb') == 3_750_000
assert parse_bytes('465GiB') == 499289948160
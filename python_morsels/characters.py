# characters.py
"""
A script implementing the function `characters()` that will convert the input string characters into lowercase and return a list of them.
Optional argument `sort` will return a sorted list.
"""

def characters(my_string: str, sort: bool = False) -> list[str]:
    return list(my_string.lower()) if not sort else sorted(list(my_string.lower()))


# base problem
assert characters('hello') == ['h', 'e', 'l', 'l', 'o']
assert characters("Drew Gooden") == ['d', 'r', 'e', 'w', ' ', 'g', 'o', 'o', 'd', 'e', 'n']

# bonus 1
assert characters("Drew Gooden", sort=True) == [' ', 'd', 'd', 'e', 'e', 'g', 'n', 'o', 'o', 'r', 'w']
assert characters('hello', sort=True) == ['e', 'h', 'l', 'l', 'o']
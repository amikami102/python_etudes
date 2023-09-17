# matrix_from_string.py
"""
A script defining `matrix_from_string()` function.
"""
from textwrap import dedent

def matrix_from_string(string) -> list[list[float]]:
    """Convert string-based rows of numbers to list of lists."""
    return [
        [float(n) for n in line.split()]
        for line in dedent(string).splitlines()
        if line
    ]


# base problem
assert matrix_from_string("3 4 5") == [[3.0, 4.0, 5.0]]
assert matrix_from_string("3 4 5\n6 7 8") == [[3.0, 4.0, 5.0], [6.0, 7.0, 8.0]]

# bonus 1, test extra white spaces
assert matrix_from_string("""
    1   2   3
    
    4   5   6
    
    7   8   9
""") == [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
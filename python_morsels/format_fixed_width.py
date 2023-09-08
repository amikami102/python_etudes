# format_fixed_width.py
"""
A script defining `format_fixed_width()` function that accepts rows of columns as list of lists
and returns a fixed-width formated string representing the given rows.

Assume that the nested lists in the input list have the same length.
"""
from typing import *


def format_fixed_width(
        rows_of_columns: list[list[str]],
        *,
        padding: int = 2,
        widths: list[int] = None,
        alignments: list[str] = None
    ) -> str:
    """
    Return multiline string where each line is a row and there are at least two white spaces between left-justified columns.
    
    Args
    ----
        rows_of_columns: list[list[str]]
            list of rows, which are lists of each row's column entries
            
        padding: int, default 2
            the number of white spaces between each columns after their widths are fixed
        
        widths: list[int], default None
            the list of custom column widths; if None, each column is as wide as its widest element
        
        alignments: list[str], default None
            the list of 'L' or 'R' indicating whether the column should be (L)eft or (R)ight justified
    """
    rows_of_columns = [
        [str(col) for col in row]
        for row in rows_of_columns
    ]
    
    if not widths:
        try:
            widths = [0] * len(rows_of_columns[0])
        except:
            widths = []	# this happens when `rows_of_columns` is an empty list
    if not alignments:
        try:
            alignments = ['L'] * len(rows_of_columns[0])
        except:
            alignments = [] # this happens when `rows_of_columns` is an empty list

    cols_fixed = []
    for *rows, custom_width, align in zip(*rows_of_columns, widths, alignments):
        width = max(
            len(max(rows, key=len)),
            custom_width
        )
        cols_fixed.append(
            [
                cell.ljust(width, ' ') if align == 'L' else cell.rjust(width, ' ')
                for cell in rows
            ]
        )
    spacing = ' ' * padding
    return '\n'.join([spacing.join(cells).rstrip() for cells in zip(*cols_fixed)])
        
        
# base problem, test `format_fixed_width()`
assert format_fixed_width([['green', 'red'], ['blue', 'purple']]) == 'green  red\nblue   purple'
assert format_fixed_width([]) == ""
assert format_fixed_width([["hi", "there"]]) == "hi  there"

# bonus 1, test the optional keyword `padding`
from textwrap import dedent
rows = [['Robyn', 'Henry', 'Lawrence'], ['John', 'Barbara', 'Gross'], ['Jennifer', '', 'Bixler']]
assert format_fixed_width(rows) ==\
   dedent(
        """
        Robyn     Henry    Lawrence
        John      Barbara  Gross
        Jennifer           Bixler
        """
    ).strip('\n')
assert format_fixed_width(rows, padding=1) ==\
    dedent(
        """
        Robyn    Henry   Lawrence
        John     Barbara Gross
        Jennifer         Bixler
        """
    ).strip('\n')

assert format_fixed_width(rows, padding=3) ==\
    dedent(
        """
        Robyn      Henry     Lawrence
        John       Barbara   Gross
        Jennifer             Bixler
        """
    ).strip('\n')

# bonus 2, test the optional keyword argument `widths`
rows = [["Jane", "", "Austen"], ["Samuel", "Langhorne", "Clemens"]]
assert format_fixed_width(rows, widths=[10, 10, 10]) ==\
    dedent(
        """
        Jane                    Austen
        Samuel      Langhorne   Clemens
        """
    ).strip('\n')

# bonus 3, test the optional keyword argument `alignements`
rows = [["Jane", "", "Austen"], ["Samuel", "Langhorne", "Clemens"]]
assert format_fixed_width(rows, alignments=['R', 'L', 'R']) ==\
    dedent(
        """
          Jane              Austen
        Samuel  Langhorne  Clemens
        """
    ).strip('\n')

# line_numbers.py
"""
A program that prints out the lines in the given file.
"""
import sys


for file in sys.argv[1:]:
    with open(file, 'r') as f:
        for line_num, line in enumerate(f, start=1):
            print(line_num, line.rstrip('\n'))

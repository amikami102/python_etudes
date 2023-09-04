# checksum.py
"""
A program that accepts an md5 checksum file and prints out whether each file in the checksum passes the test.

Usage example:
    $ python checksum.py sums.md5
"""
from typing import *
import argparse
import hashlib


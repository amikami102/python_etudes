# iconv.py
"""
A program that converts a text file's character encoding.

Usage example:
    $ python iconv.py utf8_file.txt -f utf-8 -o utf16le_file.txt -t utf-16le
    $ python iconv.py utf8_file.txt --from-code=utf-8 --output=utf16le_file.txt --to-code=utf-16le
    $ python iconv.py utf16le_file.txt -f utf-16le
"""
import argparse
import sys


parser = argparse.ArgumentParser("Convert a file's character encoding")
parser.add_argument('file', help='input file',
                    type=argparse.FileType('r'), default='-', nargs='?')
parser.add_argument('--from-code', '-f', help='encoding of original file')
parser.add_argument('--to-code', '-t', help='encoding of output')
parser.add_argument('--output', '-o', help='output file',
                    type=argparse.FileType('w'), default='-')
args = parser.parse_args()


args.file.reconfigure(encoding=args.from_code)
args.output.reconfigure(encoding=args.to_code)

for line in args.file:
        args.output.write(line)    

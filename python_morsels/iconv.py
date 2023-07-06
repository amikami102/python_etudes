# iconv.py
"""
A program that converts a text file's character encoding like Linux CLI tool's `iconv`.

Usage example:
    $ python iconv.py utf8_file.txt -f utf-8 -o utf16le_file.txt -t utf-16le
    $ python iconv.py utf8_file.txt --from-code=utf-8 --output=utf16le_file.txt --to-code=utf-16le
    $ python iconv.py utf16le_file.txt -f utf-16le
"""
import argparse
import sys

parser = argparse.ArgumentParser("Convert a file's character encoding")
parser.add_argument('input', type=str, nargs='?')
parser.add_argument('--from-code', '-f', type=str, default='utf-8')
parser.add_argument('--to-code', '-t', type=str, default='utf-8')
parser.add_argument('--output', '-o', type=argparse.FileType('w'), default='-')
args = parser.parse_args()


data = open(args.input, mode='rb').read().decode(args.from_code)
args.output.reconfigure(encoding=args.to_code)
args.output.write(data)
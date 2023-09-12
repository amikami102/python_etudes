# gz.py
"""
A program that will compress a given file into a gz file.
If given an optional '-d' flag, the program will decompress the given file.

Usage example
    $ python gz.py zen.txt
    $ python gz.py -d zen.txt.gz
"""
import gzip
from pathlib import Path
import argparse
from io import DEFAULT_BUFFER_SIZE


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=Path)
    parser.add_argument('-d', '--decompress', action='store_true')
    args = parser.parse_args()
    
    if args.decompress:
        # decompress the given file
        read_file = gzip.open(args.filepath, mode='rb')
        write_file = args.filepath.with_suffix('').open(mode='wb')
            
    else:
        # compress the given file
        read_file = args.filepath.open(mode='rb')
        gzip_filepath = args.filepath.with_suffix(args.filepath.suffix + '.gz')
        write_file = gzip.open(gzip_filepath, 'wb')
    
    while chunk := read_file.read(DEFAULT_BUFFER_SIZE):
        write_file.write(chunk)
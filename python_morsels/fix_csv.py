# fix_csv.py
"""
A program that noramlizes CSV files by converting a file into a comma-delimited file.

Usage example:
    $ python fix_csv.py cars-original.csv cars.csv
    $ python fix_csv.py --in-delimiter="|" cars.csv cars-fixed.csv
    $ python fix_csv.py cars.csv cars-fixed.csv --in-delimiter="|"
    $ python fix_csv.py --in-delimiter="|" --in-quote="'" cars.csv cars-fixed.csv
    $ python fix_csv.py --in-quote="|" --in-delimiter="," cars.csv cars-fixed.csv
"""
import argparse
import csv
from pathlib import Path


if __name__ == '__main__':

    parser = argparse.ArgumentParser('Normalize CSV files')
    parser.add_argument('infile', type=argparse.FileType('r'), nargs='?')
    parser.add_argument('outfile', type=argparse.FileType('w'), nargs='?')
    parser.add_argument('--in-delimiter', type=str)
    parser.add_argument('--in-quote', type=str)
    args = parser.parse_args()
    
    # read the data from the input file
    if args.in_delimiter or args.in_quote:
        kwargs = {
            'delimiter': '|' if not args.in_delimiter else args.in_delimiter,
            'quotechar': '"' if not args.in_quote else args.in_quote
        }
    else:
        kwargs = {'dialect': csv.Sniffer().sniff(args.infile.read(1024))}
        args.infile.seek(0)
    data = csv.reader(args.infile, **kwargs)
    
    # write the data as comma-separated values in the output file
    writer = csv.writer(args.outfile, delimiter=',')
    writer.writerows(data)

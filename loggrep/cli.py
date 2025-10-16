#!/usr/bin/env python3 

import argparse #Import the library argparse to recognize flags and commands from the command line
from .core import read_and_find_normal #Import a function from core.py-main logic for this package.

def main():
    parser = argparse.ArgumentParser(
            prog='loggrep',
            description='Like grep but shittier, can be used or improved tailored for specific purposes')

    parser.add_argument('filepath', help='The file inside the current directory or the path of the file you want to analyze')
    parser.add_argument('pattern', help='The pattern you want to look for inside a file')
    parser.add_argument('-c', '--count', help='Additional option that will add in later') #Additional option for this package

    arguments = parser.parse_args() #Place the data inside the namespace arguments

    file = arguments.filepath
    pattern = arguments.pattern
    option = arguments.count

    if option is None:      
        read_and_find_normal(filepath, pattern) #Default option if none is provided

if __name__ == "__main__":
    main()

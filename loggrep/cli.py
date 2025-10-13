#!/usr/bin/env python3 
import argparse
from .core import read_and_find_normal

def main():
    parser = argparse.ArgumentParser(description='Like grep but shittier')

    parser.add_argument('file', help='The file inside the current directory or the path of the file you want to analyze')

    parser.add_argument('pattern', help='The pattern you want to look for inside a file')

    arguments = parser.parse_args()

    file = arguments.file
    pattern = arguments.pattern

    read_and_find_normal(file, pattern)

if __name__ == "__main__":
    main()

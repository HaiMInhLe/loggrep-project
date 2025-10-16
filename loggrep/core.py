#!/usr/bin/env python3
import re

def read_and_find_normal(document, pattern):
    with open(document, "r") as file:               #Creat a file object that connect to the actual file, whose path is stored inside "document"
                                                    #the "with" statement is called a context manager,  just a shorter to say open and close the file

        for num, line in enumerate(file, start=1):  #Read line by line, and use enumerate to get the index of the line
            if re.search(pattern, line, re.I):      #Check if the pattern is in the line, and make it case insensitive.
                print(f"{num}: {line.strip()}")                 #Print out the line contains the pattern

#def read_and_find_pepperoni(document, pattern):
#    with open(document, "r") as file:               #Creat a file object that connect to the actual file, whose path is stored inside "document"
#        for num, line in enumerate(file, start=1):
#            if re.





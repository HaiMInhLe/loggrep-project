#!/usr/bin/env python3

def read_and_find(document, pattern):
    with open(document, "r") as file:               #Creat a file object that connect to the actual file, whose path is stored inside "document"
                                                    #the "with" statement is called a context manager,  just a shorter to say open and close the file

        for num, line in enumerate(file, start=1):  #Read line by line, and use enumerate to get the index of the line

            if pattern.lower() in line.lower():     #Check if the pattern is in the line, and make it case insensitivity
                
                print(f"{num}: {line.strip()}")                 #Print out the line contains the pattern

def main():
    doc = input()
    pattern = input()
    read_and_find(doc, pattern)

if __name__ == "__main__":
    main()


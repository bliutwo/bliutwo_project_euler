# File: LargeSum.py
# Description: takes in a data file of a list of ints and outputs the sum

import argparse

def readParseAndReturnListOfInts(filename):
    openedFile = open(filename, "r")
    listOfInts = []
    for line in openedFile:
        listOfInts.append(int(line))
    openedFile.close()
    return listOfInts

def main():
    # takes in 3 command line arguments
    parser = argparse.ArgumentParser(description='reads in [data.txt] and adds the numbers in it')
    parser.add_argument("filename", help = "enter the filepath of a [data.txt] file")
    args = parser.parse_args()
    # read in and parse each line to make a list of ints
    total = 0;
    listOfInts = readParseAndReturnListOfInts(args.filename)
    for num in listOfInts:
        total += num
    print "total is: ", total

if __name__ == "__main__":
    main()

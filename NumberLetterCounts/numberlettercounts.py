#!/usr/bin/env python -B
# Filename: numberlettercounts.py
# Description: Counts the number of letters used for numbers from 1 to
#              1000 

import sys
sys.dont_write_bytecode = True

from numstowords import *

def main():
    PEPE = raw_input("What number would you like to convert? (Type 'e' to exit) ")
    while (PEPE != 'e'):
        word = numToWord(int(PEPE))
        print word
        PEPE = raw_input("What number would you like to convert? (Type 'e' to exit) ")
    print "exiting.."

if __name__ == "__main__":
    main()

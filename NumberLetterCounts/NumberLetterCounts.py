#!/usr/bin/env python -B
# Filename: NumberLetterCounts.py
# Description: Counts the number of letters used for numbers from 1 to
#              1000 

import sys

sys.dont_write_bytecode = True

from numsToWords import *

def main():
	PEPE = input("What number would you like to convert? ")
	word = numToWord(PEPE)
	print word

if __name__ == "__main__":
    main()

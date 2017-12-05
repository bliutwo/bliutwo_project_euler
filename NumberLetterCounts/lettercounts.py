#!/usr/bin/env python -B
# Filename: lettercounts.py
# Description: Counts the number of letters used for numbers from 1 to
#              1000 

import sys
sys.dont_write_bytecode = True

import numstowords

def main():
    num_letters = 0
    for i in range(1,1001):
        num = numstowords.numToWord(str(i))
        num_letters += len(num)
        print "%d\t%s" % (i, num)
    print "Total letters: %d" % num_letters

if __name__ == "__main__":
    main()

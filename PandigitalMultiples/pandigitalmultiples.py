# Filename: pandigitalmultiples.py
# Description: https://projecteuler.net/problem=38

import sys
sys.dont_write_bytecode = True

import time

from itertools import permutations

def all_nine_digit_pandigitals():
    x='123456789'
    perms = [''.join(p) for p in permutations(x)]
    return perms

def find_limits():
    for i in range(1,9):
        for j in range(1,9):
            
    
def main():
    print "Calculating..."
    start = time.time()

    # START CODE HERE
    l = all_nine_digit_pandigitals()
    print l

    find_limits()

    t = max(l)

    end = time.time()
    sumtime = end - start
    print "DONE!"
    print sumtime
#    print t
#    fo = open("results.txt", "wb")
#    fo.write("%d\n%.8f\n" % (t, sumtime))
#    fo.close()


if __name__ == "__main__":
    main()

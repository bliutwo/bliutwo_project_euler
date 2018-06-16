# Filename: lexicographicpermutations.py
# Description: https://projecteuler.net/problem=24

import sys
sys.dont_write_bytecode = True

import time
from itertools import permutations

def main():
    print "Calculating..."
    start = time.time()

    # START CODE HERE
    l = '0123456789'
    count = 1
#    perm = permutations(l, 10)
#    perm.sort()
    t = None

    listeroni = []
    for i in permutations(l,len(l)):
        listeroni.append(i)
    listeroni.sort()

#    print listeroni

    t = listeroni[1000000-1]


    end = time.time()
    sumtime = end - start
    print "DONE!"
    print sumtime
    print t
    fo = open("results.txt", "wb")
    fo.write("%r\n%.8f\n" % (t, sumtime))
    fo.close()


if __name__ == "__main__":
    main()

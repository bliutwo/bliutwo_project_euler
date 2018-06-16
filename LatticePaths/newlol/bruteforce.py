# Filename: latticepaths.py
# Description: https://projecteuler.net/problem=15

import sys
sys.dont_write_bytecode = True

import time
from itertools import permutations

def main():
    print "Calculating..."
    start = time.time()

    # START CODE HERE
    dimension = 6
    s = ""
    for i in range(0, dimension):
    	s += "a"
    	s += "b"
    perms = [''.join(p) for p in permutations(s)]

    t = len(set(perms))
    print t

    end = time.time()
    sumtime = end - start
    print "DONE!"
    print sumtime
    print t
    fo = open("results.txt", "wb")
    fo.write("%d\n%.8f\n" % (t, sumtime))
   # fo.close()


if __name__ == "__main__":
    main()

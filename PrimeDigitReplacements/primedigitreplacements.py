# Filename: primedigitreplacements.py
# Description: https://projecteuler.net/problem=51

import sys
sys.dont_write_bytecode = True

import time

from is_prime import is_prime
from get_primes import get_primes

def main():
    print "Calculating..."
    start = time.time()

    # START CODE HERE
    

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

# Filename: 
# Description:

import sys
sys.dont_write_bytecode = True

import time
from is_prime import is_prime
from is_circular import is_circular
from get_primes import get_primes

def main():
    print "Calculating..."
    pstart = time.time()

    primes = get_primes(2,1000000)
    
    pend = time.time()

    ptime = pend - pstart

    start = time.time()

    t = 0
    for p in primes:
        if is_circular(p):
            t+=1

    end = time.time()
    sumtime = end - start
    print "DONE!"
    print sumtime
    print t
    fo = open("results.txt", "wb")
    fo.write("%d\n%.8f\n%.8f\n" % (t, ptime, sumtime))
    fo.close()


if __name__ == "__main__":
    main()

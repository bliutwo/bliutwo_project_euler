# Filename: truncatableprimes.py
# Description: https://projecteuler.net/problem=37

import sys
sys.dont_write_bytecode = True

import time

from is_prime import is_prime
from get_primes import get_primes
from lol_truncated import truncated

def main():
    print "Calculating..."
    start = time.time()

    primes = get_primes(10,1000000)
#    print primes

    tp = []

    for p in primes:
        l = truncated(p)
        b = 1
        for n in l:
            if(not is_prime(n)):
                b = 0
                break
        if b==1:
            tp.append(p)

    print len(tp)
    assert(len(tp) == 11)

    t = sum(tp)

    end = time.time()
    sumtime = end - start
    print "DONE!"
    print sumtime
    print t
    fo = open("results.txt", "wb")
    fo.write("%d\n%.8f\n" % (t, sumtime))
    fo.close()


if __name__ == "__main__":
    main()

# Filename: pandigitalprime.py
# Description: https://projecteuler.net/problem=41

import sys
sys.dont_write_bytecode = True

import time

from itertools import permutations
from is_prime import is_prime

def create_pandigital_primes(n):
    l = []

    piss = ''
    for i in range(1,(n+1)):
        piss = piss + str(i)

#    print piss

    # https://stackoverflow.com/questions/8306654/finding-all-possible-permutations-of-a-given-string-in-python
    perms = [''.join(p) for p in permutations(piss)]

#    print perms

    for s in perms:
        potential = int(s)
        if is_prime(potential):
            l.append(potential)

#    print l

    return l

def main():
    print "Calculating..."
    start = time.time()

    bigly = 0

    for i in range (1,10):
        l = create_pandigital_primes(i)
        if l:
            bigbigly = max(l)
            if bigbigly > bigly:
                bigly = bigbigly
    
    t = bigly

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

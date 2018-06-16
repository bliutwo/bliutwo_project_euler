# Filename: primedigitreplacements.py
# Description: https://projecteuler.net/problem=51

import sys
sys.dont_write_bytecode = True

import time

from is_prime import is_prime
from get_primes import get_primes

# TODO: finish this function
def generate_nums_of_length(length):
    l = []
    for i in range(0, 9):
        

def main():
    print "Calculating..."
    start = time.time()

    # START CODE HERE
    
    # get all numbers of length i
    # replace part of the number with the same digit, from 1 to i

    t = -1

    for i in range(1,10):
        primes = []
        l = generate_nums_of_length(i)
        for j in l:
            # TODO: need to replace part of 
            # the number with same digit, write function
            if (is_prime(j)):
                primes.append(j)
        if len(primes) == 8:
            primes.sort()
            t = primes[0]

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

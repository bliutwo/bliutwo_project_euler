# Filename: goldbachotherconjecture.py
# Description: https://projecteuler.net/problem=46

import sys
sys.dont_write_bytecode = True

import time

from is_prime import is_prime
from get_primes import get_primes

def is_odd(num):
    return (num % 2 == 1)

def get_twice_a_squares(a, b):
    l = []
    for i in range(a,b):
        l.append(2*i*i)
    return l

def get_odd_composites(a, b):
    l = []
    for i in range(a,b):
        if is_odd(i):
            if not is_prime(i):
                l.append(i)
    return l

def main():
    print "Calculating..."
    start = time.time()

    # START CODE HERE
    # composite just means it's not prime

    list_of_primes = get_primes(2,10000)

    twice_a_squares = get_twice_a_squares(1,100)

    l = []
    for prime in list_of_primes:
        for tas in twice_a_squares:
            l.append(prime + tas)

    t = 0
    odd_composites = get_odd_composites(3, l[len(l)-1])
    for n in odd_composites:
        if n not in l:
            t = n
            break

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

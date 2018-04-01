# Filename: is_prime.py
# Description: Get a list of prime numbers in range (a,b)

import sys
sys.dont_write_bytecode = True

from is_prime import is_prime

def get_primes(a, b):
    l = []
    for i in range(a, (b+1)):
        if is_prime(i):
            l.append(i)
    return l

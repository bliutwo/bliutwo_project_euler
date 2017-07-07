# Filename: is_prime.py
# Description: Determine whether an integer is prime

import sys
sys.dont_write_bytecode = True

from is_prime import is_prime

def get_primes(a, b):
    l = []
    for i in range(a, (b+1)):
        if is_prime(i):
            l.append(i)
    return l

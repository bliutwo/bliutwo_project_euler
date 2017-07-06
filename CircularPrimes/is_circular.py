# Filename: is_circular.py
# Description: Determine whether an integer is circular, as defined here:
#              https://projecteuler.net/problem=35

import sys
sys.dont_write_bytecode = True

from is_prime import is_prime
from produce_circulars import produce_circulars

def is_circular(n):
    l = produce_circulars(n)
    for i in l:
        if not is_prime(i):
            return False
    return True

def main():
    a = 197
    print "%d is circular: %r" % (a, is_circular(a))
    b = 19
    print "%d is circular: %r" % (b, is_circular(b))
    c = 204
    print "%d is circular: %r" % (c, is_circular(c))

if __name__ == "__main__":
    main()

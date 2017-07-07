# Filename: is_prime.py
# Description: Determine whether an integer is prime

import sys
sys.dont_write_bytecode = True

from math import sqrt
from itertools import count, islice

# https://stackoverflow.com/a/27946768
def is_prime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def main():
    for i in range(2, 100):
        if is_prime(i):
            print i
#        print "%d\t%r" % (i, is_prime(int(i)))

if __name__ == "__main__":
    main()

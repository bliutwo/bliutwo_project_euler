# Filename: prime_factors.py
# Description: get prime factors

import sys
sys.dont_write_bytecode = True

import time

from sets import Set

# https://stackoverflow.com/questions/15347174/python-finding-prime-factors
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# https://stackoverflow.com/questions/15347174/python-finding-prime-factors
def prime_factors_mod(n):
    i = 2
    factors = set()
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.add(i)
    if n > 1:
        factors.add(n)
    return factors

def main():
    print "Calculating..."
    start = time.time()

    cons = [14, 15, 644, 645, 646]
    for n in cons:
        print prime_factors(n)
        print prime_factors_mod(n)

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

# Filename: distinctprimesfactors.py
# Description: https://projecteuler.net/problem=47

import sys
sys.dont_write_bytecode = True

import time
from prime_factors import prime_factors_mod

def dpf(n, l):
    for i in l:
        a = prime_factors_mod(i)
        if len(a) != n:
            return False
    return True
       
def distinct_primes_factors(n, r):
    l = []
    for i in range(0, len(r)-n):
        q = []
        for j in range(0,n):
            q.append(r[i+j])
        if dpf(n, q):
            return q
            break
    return l


def main():
    print "Calculating..."
    start = time.time()

    l = [x for x in range(1000000)]

    tdpf = distinct_primes_factors(2, l)
    print tdpf

    trdpf = distinct_primes_factors(3, l)
    print trdpf

    fdpf = distinct_primes_factors(4, l)
    print fdpf

    t = fdpf[0]

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

# Filename: combinatoricselections.py
# Description: https://projecteuler.net/problem=53

import sys
sys.dont_write_bytecode = True

import time

import operator as op
# https://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom

def ncr_gr_one_mil(n):
    total = 0
    for i in range(0, (n+1)):
        c = ncr(n,i)
        if c > 1000000:
            total += 1
    return total

def main():
    print "Calculating..."
    start = time.time()

    t = 0
    for i in range(1, 101):
        t += ncr_gr_one_mil(i)

    end = time.time()
    sumtime = end - start
    print "DONE!"
    print sumtime
    fo = open("results.txt", "wb")
    fo.write("%d\n%.8f\n" % (t, sumtime))
    fo.close()


if __name__ == "__main__":
    main()

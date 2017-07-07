# Filename: quadraticprimes.py
# Description: https://projecteuler.net/problem=27

import sys
sys.dont_write_bytecode = True

import time
from is_prime import is_prime

def formula(n, a, b):
    return (n*n) + (a*n) + b

def num_cons_pr(a, b):
    l = []
    n = 0
    while True:
        pp = formula(n, a, b)
        if is_prime(pp):
            n+=1
            l.append(pp)
        else:
            break
    return l

def main():
    print "Calculating..."
    start = time.time()

    maxConsPr = 0
    t = 0

    s = 1000
    e = 1000000

    for a in range((s+1), e):
        for b in range(s, e):
            l = num_cons_pr(a, b)
            ncp = len(l)
            if ncp > maxConsPr:
                print a, b
                print l, len(l)
                maxConsPr = ncp
                t = a*b


    end = time.time()
    sumtime = end - start
    print "DONE!"
    print sumtime
    print t
    fo = open("e_results.txt", "wb")
    fo.write("%d\n%.8f\n" % (t, sumtime))
    fo.close()


if __name__ == "__main__":
    main()

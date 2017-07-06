# Filename: permutedmultiples.py
# Description: https://projecteuler.net/problem=52

import sys
sys.dont_write_bytecode = True

import time
import collections

# https://stackoverflow.com/a/396438
def is_not_permutation(a, b):
    d = collections.defaultdict(int)
    for x in a:
        d[x] += 1
    for x in b:
        d[x] -= 1
    return any(d.itervalues())

def permuted_multiple(n):
    l = []
    for i in range(2, 7):
        l.append(str(i * n))
    sn = str(n)
    for s in l:
        if(is_not_permutation(sn, s)):
            return False
    return True

def main():
    print "Calculating..."
    start = time.time()

    i = 1
    while(True):
        if(permuted_multiple(i)):
            break
        i += 1

    end = time.time()
    sumtime = end - start
    print "DONE!"
    print sumtime
    fo = open("results.txt", "wb")
    fo.write("%d\n%.8f\n" % (i, sumtime))
    fo.close()


if __name__ == "__main__":
    main()

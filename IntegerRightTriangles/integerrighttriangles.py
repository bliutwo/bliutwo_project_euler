# Filename: integerrighttriangles.py
# Description: https://projecteuler.net/problem=39

import sys
sys.dont_write_bytecode = True

import time
from try_per import try_per

def main():
    print "Calculating..."
    start = time.time()

    perim = 0
    maxsol = 0

    for p in range(3, 1001):
        sol = try_per(p)
        if sol > maxsol:
            maxsol = sol
            perim = p
#            print "maxsol: %d\t perim: %d" % (maxsol, perim)

    t = perim

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

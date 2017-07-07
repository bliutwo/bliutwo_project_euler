# Filename: numberspiraldiagonals.py
# Description: https://projecteuler.net/problem=28

import sys
sys.dont_write_bytecode = True

import time

def main():
    print "Calculating..."
    start = time.time()

    l = []
    
    n = 1
    l.append(n)

    d = 1001
    e = (d-1)/2
    for a in range(0,e):
        mult = 2 * (a + 1)
        for i in range(0,4):
            n += mult
            l.append(n)

    print l 

    t = sum(l)

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

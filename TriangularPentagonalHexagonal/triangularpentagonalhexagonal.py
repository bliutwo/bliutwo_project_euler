# Filename: triangularpentagonalhexagonal.py
# Description: https://projecteuler.net/problem=45

import sys
sys.dont_write_bytecode = True

import time

def triangulars(a, b):
    l = []
    for n in range(a, b):
        tn = (n*(n+1))/2
        l.append(tn)
    return l

def pentagonals(a, b):
    l = []
    for n in range(a, b):
        tn = (n*(3*n-1))/2
        l.append(tn)
    return l

def hexagonals(a, b):
    l = []
    for n in range(a, b):
        tn = n*(2*n-1)
        l.append(tn)
    return l

def main():
#    print triangulars(1,6)
#    print pentagonals(1,6)
#    print hexagonals(1,6)
    print "Calculating..."
    start = time.time()

    tria = triangulars(286,100000)
    pent = pentagonals(166,100000)
    hexa = hexagonals(144,100000)

    t = 0

    for n in tria:
        if n in pent and n in hexa:
            t = n
            break

    end = time.time()
    sumtime = end - start
    print "DONE!"
    print sumtime
    print t
    fo = open("a_other_results.txt", "wb")
    fo.write("%d\n%.8f\n" % (t, sumtime))
    fo.close()


if __name__ == "__main__":
    main()

# Filename: digitfifthpowers.py
# Description: https://projecteuler.net/problem=30

import sys
sys.dont_write_bytecode = True

import time

def sum_of_fifths(i):
    s = str(i)
    l = []
    for d in s:
        it = int(d)
        fifth = it ** 5
        l.append(fifth)
    return sum(l)

def main():
    print "Calculating..."
    start = time.time()
    l = []
    for i in range(2, 1000000):
        s = sum_of_fifths(i)
        if s == i:
            l.append(i)
    print l
    t = sum(l)
    end = time.time()
    sumtime = end - start
    print "DONE!"
    print "%d\n%.8f" % (t, sumtime)
    fo = open("results.txt", "wb")
    fo.write("%d\n%.8f\n" % (t, sumtime))
    fo.close()

if __name__ == "__main__":
    main()

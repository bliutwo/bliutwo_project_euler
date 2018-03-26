# Filename: triangulars.py
# Description: takes an integer, outputs two columns:
#              numbers up to the integer, its triangular number

import sys
sys.dont_write_bytecode = True

import time

def triangle(n):
    r = 0
    for i in range(0, n + 1):
        r += i
    return r

def triangular(num):
    for i in range(1,(num+1)):
        print "%d\t%d" % (i, triangle(i))

def main():
    print "Calculating..."
    start = time.time()

    # START CODE HERE

    triangular(20)

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

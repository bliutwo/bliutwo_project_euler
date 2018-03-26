# Filename: totientmaximum.py
# Description: https://projecteuler.net/problem=69

import sys
sys.dont_write_bytecode = True

import time

from multiples import multiples

def totient(n):

    return 0

def main():
    if len(sys.argv) != 2:
        print "Usage: Py -2 totientmaximum.py [integer]"
    else:  
        print "Calculating..."
        start = time.time()

        # START CODE HERE

        u = sys.argv[1]

        t = ""

        t = "The Totient output for %d is: %d" % (int(u), totient(int(u)))
        print t

        end = time.time()
        sumtime = end - start
        print "DONE!"
        print sumtime
        print t
        fo = open("results.txt", "wb")
        fo.write("%s\n%.8f\n" % (t, sumtime))
        fo.close()


if __name__ == "__main__":
    main()

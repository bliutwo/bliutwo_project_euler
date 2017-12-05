# Filename: countingsundays.py
# Description: https://projecteuler.net/problem=19

import sys
sys.dont_write_bytecode = True

import time

def main():
    print "Calculating..."
    start = time.time()

    # START CODE HERE

    # current date
    year = 1900
    day = 1
    month = 1
    # day of week
    dow = 1

    # limits
    max_months = 12
    max_dow = 7



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

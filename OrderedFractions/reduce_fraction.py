# Filename: reduce_fraction.py
# Description: Takes two integers, a and b, and returns two integers, c and d,
#              such that c/d is the reduced fraction form of a/b

import sys
sys.dont_write_bytecode = True

import time

def reduce_fraction(a, b):
    l = []
    
    return l

def main():
    print "Calculating..."
    start = time.time()

    # START CODE HERE
    p = "Input numerator ('e' to exit): "
    q = "Input denominator: "

    u = raw_input(p)
    while u != 'e':
        v = raw_input(q)
        lp = reduce_fraction(int(u), int(v))
        print "%d/%d as a reduced fraction is: %d/%d" % (int(u), int(v), lp[0], lp[1])
        u = raw_input(p)
  


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

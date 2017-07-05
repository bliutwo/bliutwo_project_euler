# Filename: doublebasepalindromes.py
# Description: https://projecteuler.net/problem=36

import sys
sys.dont_write_bytecode = True

import time

def main():
    start = time.time()
    l = []
    print "Adding in progress..."
    for i in range(0, 1000000):
#        print i
        s = str(i)
        b = "{0:b}".format(i)
        rs = s[::-1]
        rb = b[::-1]
#        print "%s : %s" % (s, rs)
#        print "%s : %s" % (b, rb)
        if s == rs and b == rb:
            l.append(i)
#            print "Yes!"
#        print
    end = time.time()
    total = sum(l)
    print total
    print "%.8f" % (end - start)

    fo = open("results.txt", "wb")
    fo.write("%d\n%.8f\n" % (total, (end-start)))
    fo.close()

    
if __name__ == "__main__":
    main()

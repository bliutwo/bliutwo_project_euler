# Filename: primepermutations.py
# Description: https://projecteuler.net/problem=49

import sys
sys.dont_write_bytecode = True

import time
from is_prime import is_prime

def main():
    print "Calculating..."
    start = time.time()
    
    
    
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

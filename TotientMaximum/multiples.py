# Filename: multiples.py
# Description: Returns a list of the multiples of an integer,
#              NOT including the integer itself

import sys
sys.dont_write_bytecode = True

import time

def multiples(n):
    l = []
    for i in range(1,(n/2)+1):
        if n % i == 0:
            l.append(i)
    return l

def main():
    print "Calculating..."
    start = time.time()

    # START CODE HERE

    p = "Input integer ('e' to exit): "

    u = raw_input(p)

    while u != 'e':
        print "%d has these multiples: " % int(u)
        print multiples(int(u))
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

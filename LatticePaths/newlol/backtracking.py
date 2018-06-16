# Filename: backtracking.py
# Description: Sees if we've seen this path before, if we have, then don't go down it

import sys
sys.dont_write_bytecode = True

import time

def findpaths(s, paths):
	l = []
	return l

def main():
    print "Calculating..."
    start = time.time()

    # START CODE HERE
    dimension = 3
    s = ""
    for i in range(0, dimension):
    	s += "a"
    	s += "b"

    paths = set()

    findpaths(s, paths)

    t = len(paths)


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

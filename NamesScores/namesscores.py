# Filename: namesscores.py
# Description: https://projecteuler.net/problem=22

import sys
sys.dont_write_bytecode = True

import time
from alphanumdict import alphanumdict
import str_list

def main():
    print "Calculating..."
    start = time.time()

    d = alphanumdict()

    fname = "p022_names.txt"

    l = str_list.get_file_str_list(fname)
    l.sort()
    
    i = 0
    ns = []
    for s in l:
        i += 1
        ns.append(str_list.get_alphanum_value(s,d)* i)

    t = sum(ns)

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

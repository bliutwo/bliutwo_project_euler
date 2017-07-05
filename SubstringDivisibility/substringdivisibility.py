# Filename: substringdivisibility.py
# Description: https://projecteuler.net/problem=43

import sys
sys.dont_write_bytecode = True

import time
from itertools import permutations

def get_all_pandigitals(a, b):
    l = ""
    for i in range(a,b+1):
        l = l + str(i)
    perms = [''.join(p) for p in permutations(l)]
    tp = []
    for p in perms:
        if p[0] != '0':
            tp.append(p)
    return tp

def check_property(s):
    n1 = int(s[1:4])
    n2 = int(s[2:5])
    n3 = int(s[3:6])
    n4 = int(s[4:7])
    n5 = int(s[5:8])
    n6 = int(s[6:9])
    n7 = int(s[7:10])
    if n1 % 2 != 0:
        return False
    if n2 % 3 != 0:
        return False
    if n3 % 5 != 0:
        return False
    if n4 % 7 != 0:
        return False
    if n5 % 11 != 0:
        return False
    if n6 % 13 != 0:
        return False
    if n7 % 17 != 0:
        return False
    return True

def main():
    print "Calculating..."
    start = time.time()
    l = get_all_pandigitals(0, 9)
    a = []
    for s in l:
        if check_property(s):
            a.append(int(s))
    t = sum(a)
    end = time.time()
    sumtime = end - start
    print "DONE!"
    print sumtime
    fo = open("results.txt", "wb")
    fo.write("%d\n%.8f\n" % (t, sumtime))
    fo.close()


if __name__ == "__main__":
    main()

# Filename: primepermutations.py
# Description: https://projecteuler.net/problem=49

import sys
sys.dont_write_bytecode = True

import time
from is_prime import is_prime
from itertools import permutations
from itertools import combinations

def diff_same(subset):
    l = []
    for e in subset:
        l.append(int(e))
    l.sort()
    if l[2] - l[1] == l[1] - l[0]:
        return True
    return False

def all_digits_diff(i):
    s = str(i)
    if s[0] == s[1]:
        return False
    if s[0] == s[2]:
        return False
    if s[0] == s[3]:
        return False
    if s[1] == s[2]:
        return False
    if s[1] == s[3]:
        return False
    if s[2] == s[3]:
        return False
    return True

# not all equal
def nae(subset):
    if subset[0] == subset[1]:
        return False
    if subset[1] == subset[2]:
        return False
    if subset[0] == subset[2]:
        return False
    return True

def primeperm(allfdq):
    for q in allfdq:
        # https://stackoverflow.com/questions/8306654/finding-all-possible-permutations-of-a-given-string-in-python
        perms = [''.join(p) for p in permutations(q)]
        for subset in combinations(perms, 3):
            if all(int(elem) > 999 and is_prime(int(elem)) for elem in subset):
                if nae(subset):
                    if diff_same(subset):
                        if '1487' not in subset:
                            return subset

def main():
    print "Calculating..."
    start = time.time()

    allfdq = []

    for i in range(1000,10000):
        if is_prime(i): #and all_digits_diff(i):
            allfdq.append(str(i))

    l = primeperm(allfdq)

    print l

    sl = []
    for e in l:
        sl.append(int(e))

    sl.sort()

    s = ''
    for e in sl:
        s = s + str(e)
    
    print s

    t = int(s)
    
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

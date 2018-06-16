# Filename: totientmaximum.py
# Description: https://projecteuler.net/problem=69
# TODO: the problem is that it takes too long - maybe multithreading?

import sys
sys.dont_write_bytecode = True

import time

from multiples import multiples

# https://stackoverflow.com/questions/2864842/common-elements-comparison-between-2-lists
# gets list of common elements between two lists
def get_common_elems(list1, list2):
    return list(set(list1).intersection(list2))

# checks if two numbers are relatively prime
# that is, if the only positive integer (factor) that divides both of them is 1
def relatively_prime(a, b):
    # get all factors for both
    # check if each list has only 1 in common
    am = multiples(a)
    bm = multiples(b)
    l = get_common_elems(am,bm)
    return len(l) == 1
    
# so called phi function
def totient(n):
    l = []
    for i in range (1,n):
        if relatively_prime(i, n):
            l.append(i)
    return len(l)

def main():
#    if len(sys.argv) != 2:
#        print "Usage: Py -2 totientmaximum.py [integer]"
#    else:  
    print "Calculating..."
    start = time.time()

    # START CODE HERE
    # biggest = 1000000
    biggest = 1000
#    for i in range(2,biggest+1):
#        t = "The Totient output for %d is: %d\t%.5f" % (i, totient(i), float(i) / totient(i))
#        print t

    ns = []
    for i in range(2,biggest+1):
        ns.append(i)

    quotients = []
    for i in ns:
        quotients.append(float(i) / totient(i))

# https://stackoverflow.com/questions/3989016/how-to-find-all-positions-of-the-maximum-value-in-a-list
    m = max(quotients)
    a = [i for i, j in enumerate(quotients) if j == m]

    t = ns[a[0]]

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

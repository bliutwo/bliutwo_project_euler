# Filename: codedtrianglenums.py
# Description: https://projecteuler.net/problem=42

import sys
sys.dont_write_bytecode = True

import time

d = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6,
     'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12,
     'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18,
     'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24,
     'Y':25, 'Z':26}

def tri_form(n):
    return n*(n+1)/2

def make_tri_list(a,b):
    l = []
    for i in range(a,b):
        l.append(tri_form(i))
    return l
    
triangles = make_tri_list(0, 1000)

def is_triangle(t):
    return (t in triangles)

def get_triangle_value(s):
    t = 0
    for c in s:
        if c in d:
            t += d[c]
    return t

def main():
    print "Calculating..."
    start = time.time()

    l2 = []
    l = []

    fname = "p042_words.txt"

    # https://stackoverflow.com/questions/3277503/how-do-i-read-a-file-line-by-line-into-a-list
    with open(fname) as f:
        l = f.readlines()
    print len(l)
    # you may also want to remove whitespace characters
    # like '\n' at the end of each line
    s = l[0]
# https://stackoverflow.com/questions/12088442/python-how-to-separate-string-with-comma
    li = s.strip().split(",")

    print len(li)
#    print li

    for s in li:
        v = get_triangle_value(s)
#        if "SKY" in s:
#            print s, v
        if is_triangle(v):
            l2.append((s, v))

    print l2
    t = len(l2)

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

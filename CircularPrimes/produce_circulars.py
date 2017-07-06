# Filename: produce_circulars.py
# Description: Determine whether an integer is circular, as defined here:
#              https://projecteuler.net/problem=35

import sys
sys.dont_write_bytecode = True

def produce_circulars(n):
    l = []
    sn = str(n)
    for i in range(0,len(sn)):
        l.append(int(sn[i:len(sn)] + sn[0:i]))
    return l

def main():
    print 197
    print produce_circulars(197)
    print 293
    print produce_circulars(293)

if __name__ == "__main__":
    main()

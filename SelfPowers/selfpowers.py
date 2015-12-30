# Filename: selfpowers.py
# Description: https://projecteuler.net/problem=48

import sys
sys.dont_write_bytecode = True

def seriesPowers(num):
    total = 0
    for x in xrange(1, num+1):
        total += x**x
    return total

def main():
    num = input("Give a num to find the series 'self powers' of: ")
    while (num != -1):
        print "sum: %d" % seriesPowers(num)
        num = input("Give a num to find the series 'self powers' of: ")
    print "Exiting."

if __name__ == "__main__":
    main()

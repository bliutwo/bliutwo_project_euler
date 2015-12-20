# File: FactorialDigitSum.py
# Description: https://projecteuler.net/problem=20
#              Find sum of digits of n!

import sys
sys.dont_write_bytecode = True
sys.path.insert(0, '../PowerDigitSum/')
from PowerDigitSum import *
import math


def main():
    num = input("Input an integer: ")
    factorial = math.factorial(num)
    print "Sum of digits in %d! : %d" % (num, getSumDigits(factorial))

if __name__ == "__main__":
    main()

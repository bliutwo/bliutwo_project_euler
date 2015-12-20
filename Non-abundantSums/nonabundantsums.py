# File: nonabundantsums.py
# Description: https://projecteuler.net/problem=23

# Find the sum of all the positive integers which cannot be written as
# the sum of two abundant numbers.
# Abundant number: sum of its proper divisors exceeds 'number'

import sys
sys.dont_write_bytecode = True
sys.path.insert(0, '../AmicableNumbers/')
from AmicableNumbers import *
# sumOfProperDivisors(num)

def isAbundant(num):
    sumProperDivisors = sumOfProperDivisors(num)
    if sumProperDivisors > num:
        return True
    else:
        return False

# how do you find out if a number can be written as the sum of two
# abundant numbers?
# the two numbers that are in the sum must be less than num
def cantSumAbundant(num, listOfAbundantNumbers):
    return True

def getAllAbundantNumbers(small, large):
    listOfAbundantNumbers = []
    for num in xrange(small, large):
        if isAbundant(num):
            listOfAbundantNumbers.append(num)
    return listOfAbundantNumbers
    
# the smallest number that can be written as the sum of two
# abundant nums is 24
# all integers greater than 28123 can be written as the sum of two
# abundant numbers
def main():
    totalSum = 0
    # 12 is the smallest abundant number
    listOfAbundantNumbers = getAllAbundantNumbers(12, 28124)
    for num in xrange(24,28124):
        if cantSumAbundant(num, listOfAbundantNumbers):
            totalSum+=num
    print "The sum of all positive integers which cannot be written as the sum of two abundant numbers is: %d" % totalSum
    for num in xrange(1,20):
        if isAbundant(num):
            print "%d is abundant" % num
        else: 
            print "%d is deficient" % num

if __name__ == "__main__":
    main()

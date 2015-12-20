# File: nonabundantsums.py
# Description: https://projecteuler.net/problem=23

# Find the sum of all the positive integers which cannot be written as
# the sum of two abundant numbers.
# Abundant number: sum of its proper divisors exceeds 'number'

# TODO: this program takes forever to run. Why?

import sys
sys.dont_write_bytecode = True
sys.path.insert(0, '../AmicableNumbers/')
from AmicableNumbers import *
# sumOfProperDivisors(num)
# sumOfElements(samplelist)

def isAbundant(num):
    sumProperDivisors = sumOfProperDivisors(num)
    return sumProperDivisors > num

# how do you find out if a number can be written as the sum of two
# abundant numbers?
# the two numbers that are in the sum must be less than num

def getAllAbundantNumbers(small, large):
    listOfAbundantNumbers = []
    for num in xrange(small, large):
        if isAbundant(num):
            listOfAbundantNumbers.append(num)
    return listOfAbundantNumbers

def getAllAbundantNumbersSums(listOfAbundantNumbers):
    listOfAbundantNumbersSums = []
    for num in listOfAbundantNumbers:
        for snum in listOfAbundantNumbers:
            singleSum = num + snum
            listOfAbundantNumbersSums.append(singleSum)
    return listOfAbundantNumbersSums
    
# the smallest number that can be written as the sum of two
# abundant nums is 24
# all integers greater than 28123 can be written as the sum of two
# abundant numbers
def main():
    totalSum = 0
    # 12 is the smallest abundant number
    listOfAbundantNumbers = getAllAbundantNumbers(12, 28124)
    print "got list of abundant numbers"
    listOfPositiveIntegers = []
    for num in xrange(24, 28124):
        listOfPositiveIntegers.append(num)
    listOfAbundantNumbersSums = getAllAbundantNumbersSums(listOfAbundantNumbers)
    print "got list of abundant numbers sums"
    for num in listOfAbundantNumbersSums:
        if num in listOfPositiveIntegers:
            listOfPositiveIntegers.remove(num)
    print "filtered list of positive integers"
    print "The sum of all positive integers which cannot be written as the sum of two abundant numbers is: %d" %  sumOfElements(listOfPositiveIntegers)

if __name__ == "__main__":
    main()

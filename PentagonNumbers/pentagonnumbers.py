# Filename: pentagonnumbers.py
# Description: https://projecteuler.net/problem=44

import sys
sys.dont_write_bytecode = True
sys.path.insert(0, '../LongestCollatzSequence/')
from LongestCollatzSeq import printList
import math

# Check irssi logs: bpaf said you can calculate sum/diff pentagonal
# given just the numbers themselves - you don't actually have to 
# "calculate" anything

def isWhole(num):
	return (float(num)).is_integer()

# (1 + sqrt(1 + 24P))/6
def getNPlus(num):
	return (1 + math.sqrt(1 + (24 * num)))/6

def getNMinus(num):
	return (1 - math.sqrt(1 + (24 * num)))/6

# n(3n-1)/2 = (3n^2 - n)/2
def isPentagonal(num):
	return isWhole(getNPlus(num))# or isWhole(getNMinus(num))

def getPentagonNum(num):
	return (num * ((3 * num) - 1))/2

def main():
	listOfPentagonNums = []
	for num in xrange(1,10000):
		listOfPentagonNums.append(getPentagonNum(num))
	printList(listOfPentagonNums)
	diff = float("inf")
	for num in listOfPentagonNums:
		for snum in listOfPentagonNums:
			if num != snum:
				pairSum = num + snum
				pairDiff = abs(num - snum)
				if pairDiff < diff and isPentagonal(pairSum) and isPentagonal(pairDiff):
					print "Got a match - diff: %f" % pairDiff
					print "pairSum: %d ; pairDiff: %d" % (pairSum, pairDiff)
					print "num: %d ; snum: %d" % (num, snum)
					diff = pairDiff
	print "D = %f" % diff
	

if __name__ == "__main__":
	main()

# Filename: pentagonnumbers.py
# Description: https://projecteuler.net/problem=44

import sys
sys.dont_write_bytecode = True
sys.path.insert(0, '../LongestCollatzSequence/')
from LongestCollatzSeq import printList

def isWhole(num):
	return x%1 == 0

def getNPlus(num):
	return 0

def getNMinus(num):
	return 0
# n(3n-1)/2 = (3n^2 - n)/2
# TODO: WTF IS THIS SHIT - I'M TRYING TO FIND N AND I CAN'T DO IT BECAUSE OF
# IMAGINARY NUMBERS?!?!?!?!?
def isPentagonal(num):
	return isWhole(getNPlus(num)) or isWhole(getNMinus(num))

def getPentagonNum(num):
	return (num * ((3 * num) - 1))/2

def main():
	listOfPentagonNums = []
	for num in xrange(1,1000):
		listOfPentagonNums.append(getPentagonNum(num))
	printList(listOfPentagonNums)
	diff = float("inf")
	for num in listOfPentagonNums:
		for snum in listOfPentagonNums:
			if num != snum:
				pairSum = num + snum
				pairDiff = abs(num - snum)
				if pairDiff < diff and isPentagonal(pairSum) and isPentagonal(pairDiff):
					diff = pairDiff
	print "D = %f" % diff
	

if __name__ == "__main__":
	main()

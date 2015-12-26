# Filename: digitfactorials.py
# Description: https://projecteuler.net/problem=34

def factorial(num):
	total = 1
	while num > 0:
		total *= num
		num -= 1
	return total

def lengthOfNum(num):
	string = str(num)
	return len(string)

def sumOfFactorialOfDigits(num):
	total = 0
	string = str(num)
	for char in string:
		digit = int(char)
		total += factorial(digit)
	return total

def main():
# how do i know when to stop? there should be a point where
# the sum of the digits is greater than the number itself? but 3! > 3
	num = 3
	total = 0
	actualSumOfFactorialOfDigits = sumOfFactorialOfDigits(num)
# frank's hint: recursive function
# another way to do this is to simply return a boolean whether it does:
# this allows you to exit early if you know that the sum of factorial
# of digits, based on the numbers so far, will never equal the num
	while lengthOfNum(num) < lengthOfNum(actualSumOfFactorialOfDigits) + 6:
		if actualSumOfFactorialOfDigits == num:
			print "WOW: num: %d ; sum: %d" % (num, actualSumOfFactorialOfDigits)
			total += num
		num += 1
		actualSumOfFactorialOfDigits = sumOfFactorialOfDigits(num)
	print "Sum: %d" % total

if __name__ == "__main__":
	main()

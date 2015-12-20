# Filename: AmicableNumbers.py
# Description: https://projecteuler.net/problem=21
# Evaluates the sum of all the amicable numbers under 10000.
# See main for definition of amicable number.

def sumOfElements(listOfInts):
    total = 0
    for integer in listOfInts:
        total += integer
    return total

def sumOfProperDivisors(num):
    listOfProperDivisors = []
    for potentialDivisor in range(1, (num/2)+1):
        if num % potentialDivisor == 0:
            listOfProperDivisors.append(potentialDivisor)
    total = sumOfElements(listOfProperDivisors)
    return total

def main():
    # for two numbers a and b to be amicable,
    # d(a) = b and d(b) = a, where d(n) is the sum of proper divisors of n
    # both a and b are amicable numbers
    num = input("Input a number: ")
    print "sumOfProperDivisors of num: %d" % sumOfProperDivisors(num)

if __name__ == "__main__":
    main()
